# End-to-End-project-Mlops-Mlflow

# Workflows

1. Update config.yaml   # Ce fichier contient la configuration de l'application : où stocker les fichiers ; où télécharger les données ; quels dossiers créer ; où sauvegarder les modèles.

2. Update schema.yaml  # Décrit la structure des données. Il sert à vérifier que les données reçues sont conformes.

3. Update params.yaml  # hyperparamètres du modèle

4. Update the entity # classes de données (dataclasses) qui représentent la configuration. c'est une classe qui représente une structure de données utilisée dans le pipeline.

5. Update the configuration manager in src config # Son rôle est de lire les fichiers YAML et de fournir leurs valeurs au reste du programme.

6. Update the components # data ingestion, data Validation, data transformation 

7. Update the pipeline # Pipeline : tu coordonne les étapes (ordre d'execution). exple pour "Data ingestion" : Télécharge les données, les sauvegarder et lesdézipper

8. Update the main.py # lance le pipeline

9. Update the app.py # interface utilisateur (UI/API)

