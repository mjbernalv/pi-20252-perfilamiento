from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def topk_metrics_from_proba(y_true, proba, classes, ks = (1, 2, 3, 5)):
    y_true = np.asarray(y_true)
    proba = np.asarray(proba)
    class_index = {c: i for i, c in enumerate(classes)}

    y_idx = np.array([class_index[y] for y in y_true])

    n_samples = y_true.shape[0]
    results = {}

    for k in ks:
        topk_idx = np.argpartition(-proba, kth = k-1, axis = 1)[:, :k]

        hits = np.any(topk_idx == y_idx[:, None], axis = 1)
        n_hits = hits.sum()

        acc_k = n_hits / n_samples
        prec_k = n_hits / (n_samples * k)

        results[f"acc@{k}"] = acc_k
        results[f"recall@{k}"] = acc_k
        results[f"prec@{k}"] = prec_k

    return results


def evaluate_model(name, model, X, y, ks = (1, 2, 3, 5), average = "macro", plot_cm = True):
    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)
    f1 = f1_score(y, y_pred, average = average)

    print(f"Accuracy (k=1): {acc:.4f}")
    print(f"F1-{average}: {f1:.4f}")

    print("\nClassification report:")
    print(classification_report(y, y_pred))

    if not hasattr(model, "predict_proba"):
        print("\n[WARN] Model does not support predict_proba; skipping top-k metrics.")
        return {"accuracy": acc, "f1": f1}

    proba = model.predict_proba(X)
    classes = model.classes_

    topk_res = topk_metrics_from_proba(y, proba, classes, ks)

    print("\nTop-k metrics:")
    for k in ks:
        print(f"acc@{k}: {topk_res[f'acc@{k}']:.4f} | prec@{k}: {topk_res[f'prec@{k}']:.4f} | recall@{k}: {topk_res[f'recall@{k}']:.4f}")

    results = {"accuracy": acc, "f1": f1}
    results.update(topk_res)

    if plot_cm:
        cm = confusion_matrix(y, y_pred, labels = np.unique(y))
        cm_df = pd.DataFrame(cm, index = np.unique(y), columns = np.unique(y))
        plt.figure(figsize = (7, 5))
        sns.heatmap(cm_df, annot = True, fmt = "d", cmap = "Blues")
        plt.ylabel("True")
        plt.xlabel("Predicted")
        plt.title(f"Confusion Matrix - {name}")
        plt.show()

    return results