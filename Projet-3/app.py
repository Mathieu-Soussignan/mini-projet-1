import streamlit as st
from modules.orchestrator import get_utilisateurs, predict_charges
from modules.logger import logger
import altair as alt
import pandas as pd
import io

st.set_page_config(page_title="Projet 3 – Orchestration Avancée", layout="wide") # noqa

st.title("Projet 3 – Orchestration et Journalisation ")

# --------------------------------------------------------------------------------
# Section 1 : Récupération des utilisateurs (Projet 1) et affichage
# --------------------------------------------------------------------------------
st.header("1. Récupérer la liste d'utilisateurs (API Projet 1)")

if st.button("Charger la liste d'utilisateurs"):
    # Par défaut, on suppose que l'API Projet 1 est accessible sur 'http://api-proj1:8000' # noqa
    # via Docker Compose, ou 'http://localhost:8001' en local (à adapter si besoin). # noqa
    api_proj1_url = "http://api-proj1:8000"
    utilisateurs = get_utilisateurs(api_proj1_url)
    if utilisateurs is not None:
        st.write("**Liste des utilisateurs :**")
        st.write(utilisateurs)
    else:
        st.error("Impossible de récupérer les utilisateurs")

# --------------------------------------------------------------------------------
# Section 2 : Formulaire avancé pour prédiction unique (Projet 2)
# --------------------------------------------------------------------------------
st.header("2. Effectuer une prédiction de charges (API Projet 2)")

col1, col2, col3 = st.columns(3)

with col1:
    # Slider pour l'âge
    age = st.slider("Âge", min_value=0, max_value=120, value=30, step=1)
    # Slider pour le BMI
    bmi = st.slider("BMI", min_value=0.0, max_value=60.0, value=25.0, step=0.1)

with col2:
    # Sélecteur pour le sexe
    sex = st.selectbox("Sexe", ["male", "female"])
    # Sélecteur pour fumeur
    smoker = st.selectbox("Fumeur", ["yes", "no"])

with col3:
    # Nombre d'enfants
    children = st.number_input("Nombre d'enfants", min_value=0, max_value=10, value=0) # noqa
    # Région
    region = st.selectbox("Région", ["northwest", "northeast", "southwest", "southeast"]) # noqa

if st.button("Prédire (cas unique)"):
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
        st.success(f"Charges prédites : {result:.2f}")
    else:
        st.error("Échec de la prédiction")

# --------------------------------------------------------------------------------
# Section 3 : Import de données en masse pour prédictions groupées
# --------------------------------------------------------------------------------
st.header("3. Prédictions en masse (import d'un fichier CSV)")

"""
**Format attendu du CSV :**  
Les colonnes suivantes doivent être présentes :  
`age`, `bmi`, `children`, `sex`, `smoker`, `region`  # noqa
"""

uploaded_file = st.file_uploader("Importer un fichier CSV pour faire des prédictions en masse", type=["csv"]) # noqa

if uploaded_file is not None:
    # Lecture du CSV
    df_input = pd.read_csv(uploaded_file)
    st.write("Aperçu des données importées :")
    st.dataframe(df_input.head())

    # Vérification minimale des colonnes
    required_cols = {"age", "bmi", "children", "sex", "smoker", "region"}
    if not required_cols.issubset(df_input.columns):
        st.error("Le CSV ne contient pas toutes les colonnes requises.")
    else:
        if st.button("Lancer prédictions en masse"):
            api_proj2_url = "http://api-proj2:8000"
            results = []
            for _, row in df_input.iterrows():
                prediction = predict_charges(
                    api_proj2_url,
                    age=row["age"],
                    bmi=row["bmi"],
                    children=row["children"],
                    sex=row["sex"],
                    smoker=row["smoker"],
                    region=row["region"]
                )
                results.append(prediction if prediction is not None else None)

            # Ajout de la colonne "predicted_charges"
            df_input["predicted_charges"] = results
            st.success("Prédictions terminées !")
            st.dataframe(df_input.head(10))

            # Graphique rapide (distribution des charges prédites)
            st.subheader("Distribution des charges prédites")
            # On ignore les None pour le graphique
            df_graph = df_input.dropna(subset=["predicted_charges"])
            chart = alt.Chart(df_graph).mark_bar().encode(
                x=alt.X("predicted_charges:Q", bin=alt.Bin(maxbins=30)),
                y='count()'
            )
            st.altair_chart(chart, use_container_width=True)

            # Bouton pour exporter en CSV
            csv_buffer = io.StringIO()
            df_input.to_csv(csv_buffer, index=False)
            st.download_button(
                label="Télécharger les résultats en CSV",
                data=csv_buffer.getvalue(),
                file_name="predictions_mass.csv",
                mime="text/csv"
            )

# --------------------------------------------------------------------------------
# Section 4 : Conclusion et logs
# --------------------------------------------------------------------------------
st.write("Logs récents : voir le fichier de logs pour plus de détails.")
logger.info("App Streamlit (version avancée) chargée") # noqa