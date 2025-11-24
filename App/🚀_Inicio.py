import streamlit as st

def main():
    st.set_page_config(page_title = "Inicio", page_icon = "🚀", layout = 'wide')

    st.write("# Bienvenido! 👋")
    st.write("Esta es la página de inicio de la aplicación de perfilamiento de clientes. Utiliza el menú lateral para navegar entre las diferentes secciones de la aplicación.")

if __name__ == "__main__":
    main()