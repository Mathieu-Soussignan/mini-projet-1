import streamlit as st
from modules.orchestrator import get_utilisateurs, predict_charges
from modules.logger import logger

st.title("Projet 3 – Orchestration et Journalisation")

st.header("Orchestration : API Projet 1 (Patients) et API Projet 2 (Prédiction)") # noqa

# Bouton pour récupérer la liste des patients depuis Projet 1
if st.button("Récupérer la liste de patients"):
    # Dans un réseau Docker Compose, utilisez le nom du service et le port interne # noqa
    api_proj1_url = "http://api-proj1:8000"
    patients = get_utilisateurs(api_proj1_url)
    if patients is not None:
        st.write(patients)
    else:
        st.error("Impossible de récupérer les patients")

# Formulaire pour effectuer une prédiction via Projet 2
st.subheader("Effectuer une prédiction de charges")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"]) # noqa

if st.button("Prédire"):
    # Appeler le service Projet 2 via son nom de service et port interne
    api_proj2_url = "http://api-proj2:8000"
    result = predict_charges(
        api_proj2_url,
        age=age,
        bmi=bmi,
        children=children,
        sex=sex,
        smoker=smoker,
        region=region
    )
    if result is not None:
        st.success(f"Charges prédites : {result}")
    else:
        st.error("Échec de la prédiction")

st.write("Logs récents : voir le fichier de logs pour plus de détails.")

logger.info("App Streamlit chargée") # noqa