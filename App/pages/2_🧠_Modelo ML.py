from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parents[2] 

@st.cache_resource
def load_model():
    model_path = BASE_DIR / "Data"/ "refined" / "model output" / "best_hgb_model.pkl"
    with open(model_path, "rb") as f:
        model = joblib.load(model_path)
    return model


def read_clients_data():
    data_path = BASE_DIR / "Data" / "refined" / "model input" / "refined_data.csv"
    df = pd.read_csv(data_path)

    return df

def predict_client(model, df_clients):
    col1, col2, col3 = st.columns(3)
    cod_client = col1.text_input("Código del cliente")
    age_client = col2.number_input("Edad del cliente", min_value = 0, max_value = 120, step = 1)
    lst_poliza = col3.selectbox("Última póliza adquirida", df_clients['Ramo'].unique())
    list_polizas = st.multiselect("Selecciona las pólizas adquiridas", df_clients['Ramo'].unique())

    if st.button("Predecir perfil"):
        st.write(f"### Resultados de la predicción para cliente #{cod_client}")
        X_client = pd.DataFrame({
            'Edad': [age_client],
            'Ramo': [lst_poliza],
            'Salud': [1 if 'Salud' in list_polizas else 0],
            'Vida': [1 if 'Vida' in list_polizas else 0],
            'Autos': [1 if 'Autos' in list_polizas else 0], 
            'Cumplimiento': [1 if 'Cumplimiento' in list_polizas else 0],
            'Patrimoniales': [1 if 'Patrimoniales' in list_polizas else 0],
            'Otros': [1 if 'Otros' in list_polizas else 0]
        })
        st.write("**Características del cliente para la predicción**")
        st.dataframe(X_client, hide_index = True)

        st.write("")
        st.write("**Perfil predicho**")
        class_names = model.classes_
        probs = model.predict_proba(X_client)[0]
        df_probs = pd.DataFrame({
            "Clase": class_names,
            "Probabilidad": probs
        }).sort_values(by = "Probabilidad", ascending = False)
        st.dataframe(df_probs.style.format({"Probabilidad": "{:.2%}"}), hide_index = True)


def model_page():
    st.title("Modelo de aprendizaje automático (ML)")
    st.info("En esta página se describen los modelos de aprendizaje automático utilizados para el perfilamiento de clientes, incluyendo detalles sobre su entrenamiento, validación y desempeño.")

    model = load_model()
    df_clients = read_clients_data()  

    st.subheader("Predicción con el modelo HistGradientBoosting")
    predict_client(model, df_clients)


model_page()