# Ce fichier s'appelle un Dockerfile. Il décrit comment construire une image Docker pour une application

FROM python:3.8-slim-buster # Choisir l’environnement de base

RUN apt update -y && apt install awscli -y # Met à jour les packages && installe AWS CLI

WORKDIR /app # Dossier de travail dans le container (équivalent de cd /app)

COPY . /app # Copie ton projet dans le container

RUN pip install -r requirements.txt # Installe les dépendances Python

CMD ["python3", "app.py"] # Lance application 