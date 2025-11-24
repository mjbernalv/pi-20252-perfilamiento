import matplotlib.pyplot as plt
from matplotlib import colors
from pathlib import Path
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[2] 

def get_eda_data():
    data_path = BASE_DIR / "Data" / "refined" / "model input" / "refined_data.csv"
    df = pd.read_csv(data_path)
    df.drop(columns = ['codCliente', 'codPoliza', 'Edad'], inplace = True)

    return df

def plot_next_insurance(df):
    pivot = df.groupby(['Ramo', 'Y']).size().unstack(fill_value = 0)

    pivot_prop = pivot.div(pivot.sum(axis = 1), axis = 0)
    ramos_previos = pivot_prop.index.tolist()
    ramo_sel = st.selectbox("Selecciona el ramo base", options = ramos_previos)
    data = pivot_prop.loc[ramo_sel].sort_values(ascending = True) 
    data = data[data.index != ramo_sel]

    custom_colors = ["#E6EEF7", "#C1D4EA", "#8FB3D9", "#5E93C8", "#2E6EB4"]
    palette = np.linspace(0, 1, len(data))
    color_map = colors.LinearSegmentedColormap.from_list("custom_blue", custom_colors)
    bar_colors = [color_map(val) for val in palette]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.barh(
        data.index,
        data.values,
        color=bar_colors,
        edgecolor=None,
        linewidth=0
    )

    ax.set_title(
        f"Probabilidad de compra siguiente para clientes con {ramo_sel}",
        fontsize=16,
        fontweight='bold'
    )

    ax.get_xaxis().set_visible(False)

    for idx, val in enumerate(data):
        ax.text(val + 0.01, idx, f"{val*100:.1f}%", va="center")

    sns.despine(left=True, bottom=True)
    ax.grid(axis='x', linestyle='--', alpha=0.25)

    plt.tight_layout()
    st.pyplot(fig)


def eda_page():
    st.title("Análisis exploratorio de datos (EDA)")
    st.info("En está página se presentan visualizaciones y análisis descriptivos de los datos de los clientes para entender mejor sus características y comportamientos.")

    df = get_eda_data()

    st.subheader("¿Cuál es el próximo seguro más probable para este cliente?")
    plot_next_insurance(df)

eda_page()