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


# How to run this project?
### STEPS:

Clone the repository

```bash, cmd
git clone https://github.com/Amal1703/End-to-End-project-Mlops-Mlflow.git
```

### STEP 02- install the requirements
```bash, cmd
pip install -r requirements.txt
```


```bash, cmd
# Finally run the following command
python app.py
```

Now,
```bash, cmd
open up you local host and port
```



# MLflow with DagsHub

   - Sign in to DagsHub.
   - Create a new repository by clicking the "New Repository" button.
   - Click "Connect a Repository".
   - Select "Connect GitHub".
   - Authorize DagsHub to access your GitHub account.
   - Choose the GitHub repository you want to connect.
   - Once connected, your MLflow Tracking URI will be:
   https://dagshub.com/kamounamal34/End-to-End-project-Mlops-Mlflow.mlflow


