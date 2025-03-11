FROM python:3.9-slim

WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "main.py"]