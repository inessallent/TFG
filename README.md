# TFG
Este repositorio contiene el Trabajo de Fin de Grado (TFG) realizado en la Universitat Pompeu Fabra (UPF). El proyecto investiga cómo percibe la sociedad la inteligencia artificial (IA) y en qué medida está dispuesta a delegar decisiones a sistemas automatizados.

Incluye una aplicación web interactiva desarrollada para recopilar respuestas mediante un cuestionario, así como scripts para el análisis estadístico de los datos obtenidos.

**Structre code**
```plaintext
.
TFG/
├── .devcontainer/
│ └── devcontainer
├── .streamlit/
│ └── secrets
├── idiomas/
│ ├── _pycache_
│ ├── castellano.py
│ ├── catala.py
│ └── english.py
├── .Analisis/
├── app.py
├── consentiment_informat.pdf
├── datos.csv
├── graficas.R
├── README.md
├── requirements.txt
└── .gitgnore

**Tecnologías utilizadas**
- Python 3.13.1: Lenguaje principal del proyecto.
- Streamlit: Framework para la creación de aplicaciones web interactivas.
- Supabase: Base de datos en la nube (PostgreSQL) usada para almacenar las respuestas.
- R: Utilizado para el análisis estadístico y la generación de gráficos.
- Google Sheets: Para la normalización de respuestas en distintos idiomas y la preparación de gráficos simples.
