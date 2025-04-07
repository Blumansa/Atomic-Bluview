FROM python:3.11-slim

WORKDIR /app

# Copie les fichiers
COPY . .

# Installe les dépendances
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
