# Ce fichier s'appelle un Dockerfile. Il décrit comment construire une image Docker pour une application

# Choisir l’environnement de base
FROM python:3.9-slim-bookworm

# Met à jour les packages && installe AWS CLI
RUN apt update -y && apt install awscli -y 

# Dossier de travail dans le container (équivalent de cd /app)
WORKDIR /app 

# Copie ton projet dans le container
COPY . /app 

 # Installe les dépendances Python
RUN pip install -r requirements.txt 

# Lance application 
CMD ["python3", "app.py"] 