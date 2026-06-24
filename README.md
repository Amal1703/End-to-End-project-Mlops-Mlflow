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


# ???????

# AWS-CI/CD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 047616383171.dkr.ecr.us-east-2.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app





