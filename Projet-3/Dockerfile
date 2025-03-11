FROM python:3.9-slim

WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Exposer le port 8501
EXPOSE 8501

# Lancer Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]