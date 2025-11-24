# Proyecto Integrador – 2025-2
## Perfilamiento de Clientes | Maestría en Ciencias de Datos y Analítica – EAFIT
 
## Índice
 
* [Índice](#índice)
* [Descripción del proyecto](#descripción-del-proyecto)
* [Características Principales](#características-principales)
* [Acceso y ejecución del proyecto](#acceso-y-ejecución-del-proyecto)
* [Tecnologías utilizadas](#tecnologías-utilizadas)
* [Desarrolladores del Proyecto](#desarrolladores-del-proyecto)
* [Conclusión](#conclusión)
 
## Descripción del proyecto
Este repositorio presenta el Proyecto Integrador del semestre 2025-2, desarrollado por el Equipo 6 de la Maestría en Ciencias de Datos y Analítica de la Universidad EAFIT.
 
El propósito del proyecto es diseñar y evaluar un modelo de aprendizaje automático capaz de estimar la probabilidad de adquisición de seguros complementarios por parte de clientes, utilizando información proveniente de:
 
- Historial de pólizas previas.
 
- Características demográficas y de perfilamiento del cliente.
 
- Variables temporales asociadas con renovaciones, cancelaciones y periodos de vigencia.
 
El sistema predictivo se orienta a categorías de seguros como automóviles, vida y hogar, aportando una herramienta de valor para la toma de decisiones comerciales y estratégicas.
 
## Características principales
 
✔️ Pipeline de datos (ETL)
 
Incluye el desarrollo de las capas raw, trusted y refined, integrando procedimientos de depuración, estandarización, enriquecimiento y consolidación.
 
✔️ Análisis exploratorio (EDA)
 
Comprende el estudio inicial de los datos, caracterización de variables, identificación de patrones y análisis de correlaciones relevantes para el modelamiento.
 
✔️ Modelamiento predictivo
 
Contiene los experimentos, métricas y evaluación del modelo elegido, documentados mediante notebooks ejecutables.
 
## Acceso y ejecución del proyecto
1️⃣ Clonar el repositorio
 
2️⃣ Instalación de dependencias
pip install -r requirements.txt
 
3️⃣ Ejecución en Google Colab
 
Si el proyecto se ejecuta en Google Colab:
 
El proceso raw → trusted se encuentra en la sección 2.2.
 
El proceso trusted → refined corresponde a la sección 3.2.
 
En caso de ejecución local, estas secciones pueden ser comentadas para evitar dependencias externas.
 
La sección 5.2 detalla el procedimiento para la persistencia de los datos procesados dentro del entorno Colab.
 
## Tecnologías utilizadas
- Python
- Google Colab
- AWS
 
## Desarrolladores del Proyecto
- María José Bernal Vélez
- Jennifer Pino Soto
- Alejandro Olivares Restrepo
- Santiago Zapata Parra
- Jerly Alejandra Galeano Correa
 
## Conclusión
Este proyecto consolida los conocimientos adquiridos en el programa de Maestría, integrando procesos de ingeniería de datos, análisis exploratorio, modelamiento de machine learning y validación de resultados.