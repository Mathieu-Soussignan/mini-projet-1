import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn
import joblib

# --- 1. Lecture du CSV et séparation features/target ---
data = pd.read_csv("insurance.csv")

# Features : age, bmi, children, sex, smoker, region
# Target   : charges
features = data.drop("charges", axis=1)
target = data["charges"]

# --- 2. Définition du préprocesseur ---
categorical_features = ["sex", "smoker", "region"]
numeric_features = [col for col in features.columns if col not in categorical_features]  # noqa: E501

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(), categorical_features)
    ]
)

# --- 3. Division train/test ---
X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)


# --- 4. Fonction d'évaluation ---
def evaluate_model(model, X_test, y_test):
    """
    Évalue un pipeline scikit-learn sur X_test et y_test.
    Retourne RMSE, MAE, R2.
    """
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return rmse, mae, r2


# --- 5. Entraînement et logging MLflow ---
mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.set_experiment("Charges_Prediction")

# Pipeline pour la Régression Linéaire
pipeline_lr = Pipeline([
    ("preprocessor", preprocessor),
    ("lr", LinearRegression())
])

with mlflow.start_run(run_name="LinearRegression"):
    pipeline_lr.fit(X_train, y_train)
    rmse_lr, mae_lr, r2_lr = evaluate_model(pipeline_lr, X_test, y_test)
    mlflow.log_metric("rmse", rmse_lr)
    mlflow.log_metric("mae", mae_lr)
    mlflow.log_metric("r2", r2_lr)

    # Log du pipeline complet (préprocesseur + LR)
    mlflow.sklearn.log_model(pipeline_lr, "linear_regression_pipeline")
    print(f"[LinearRegression] RMSE={rmse_lr:.2f}, MAE={mae_lr:.2f}, R2={r2_lr:.2f}")  # noqa: E501

# Pipeline pour la Random Forest
pipeline_rf = Pipeline([
    ("preprocessor", preprocessor),
    ("rf", RandomForestRegressor(random_state=42))
])

with mlflow.start_run(run_name="RandomForest"):
    pipeline_rf.fit(X_train, y_train)
    rmse_rf, mae_rf, r2_rf = evaluate_model(pipeline_rf, X_test, y_test)
    mlflow.log_metric("rmse", rmse_rf)
    mlflow.log_metric("mae", mae_rf)
    mlflow.log_metric("r2", r2_rf)

    # Log du pipeline complet (préprocesseur + RF)
    mlflow.sklearn.log_model(
        pipeline_rf,
        "random_forest_pipeline",
        input_example=X_test.iloc[0:1]  # exemple d'entrée
    )
    print(f"[RandomForest] RMSE={rmse_rf:.2f}, MAE={mae_rf:.2f}, R2={r2_rf:.2f}")  # noqa: E501

# --- 6. Sauvegarde du meilleur pipeline localement ---
if rmse_rf < rmse_lr:
    joblib.dump(pipeline_rf, "best_model.pkl")
    print("Le pipeline Random Forest est sauvegardé dans 'best_model.pkl'")
else:
    joblib.dump(pipeline_lr, "best_model.pkl")
    print("Le pipeline Régression Linéaire est sauvegardé dans 'best_model.pkl'")  # noqa: E501, W292