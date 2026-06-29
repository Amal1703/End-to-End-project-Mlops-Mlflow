# End-to-End-project-Mlops-Mlflow


# How to run this project?
### STEPS:

### STEP 01 - Clone the repository

```bash, cmd
git clone https://github.com/Amal1703/End-to-End-project-Mlops-Mlflow.git
```

### STEP 02 - install the requirements
```bash, cmd
pip install -r requirements.txt
```


### STEP 03 - connect to MLflow with DagsHub 

   - Sign in to DagsHub.
   - Create a new repository by clicking the "New Repository" button.
   - Click "Connect a Repository".
   - Select "Connect GitHub".
   - Authorize DagsHub to access your GitHub account.
   - Choose the GitHub repository you want to connect.
   - Once connected, my MLflow Tracking URI will be:
   https://dagshub.com/kamounamal34/End-to-End-project-Mlops-Mlflow.mlflow
   - Modify the file mlflow_uri.py in src/mlProject/constants with your own MLflow information


### STEP 04 - run the pipeline  

```bash, cmd
python main.py
```
   - The test folder contains tests for the pipeline in main.py
   - In params.yaml, you can change the model parameters and choose a different model
   - After modifying the model parameters, select the best model. In config.yaml, under prediction_new_data:
      - model_path: define the path to the best model


### STEP 05 - run the web user interface  

```bash, cmd
python app.py
```

Now,
```bash, cmd
open up you local host and port
```


# Workflows

1. Update template.py and execute it to create the necessary project folders and files

2. Update setup.py

3. Update config.yaml   # This file contains the application configuration: where to store files, where to download data, which folders to create and where to save models.

4. Update schema.yaml  # This file describes the data structure. It is used to validate that the input data matches the expected format.

5. Update params.yaml  # This file contains the model hyperparameters

6. Update the entity # Data classes that represent the configuration. A data class is a class that represents a data structure used in the pipeline.

7. Update the configuration manager in src config # Its role is to read the YAML files and provide their values to the rest of the program.

8. Update the components # Contains the pipeline project: data ingestion, data validation, data transformation, etc.

9. Update the pipeline # This file contains the pipeline. It coordinates the different stages (execution order). For example, for "Data Ingestion": it downloads the data, saves it, and extracts the files.

10. Update the main.py # Run the pipeline

11. Update the app.py # Run the web user interface 


# AWS-CI/CD-Deployment-with-Github-Actions

## 1. Login to AWS console

	#Description about the deployment. The complete deployment process is as follows:

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

## 2. Create IAM user for deployment

	#The IAM user will have access to:

	1. EC2 access: It is a virtual machine

	 - EC2 (Elastic Compute Cloud) is an AWS service that allows you to create a virtual machine in the cloud.

	2. ECR: Elastic Container registry to save your docker image in AWS

 	 - ECR (Elastic Container Registry) is an AWS service used to store Docker images. 

 	 - A Docker image is a packaged version of the application that contains the code, dependencies and environment configuration.

	#Select the policies for the IAM user:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	#The IAM user has been created: save the Access Key and Secret Access Key or download the CSV file.
	
## 3. Create ECR repo to store/save docker image
    - Save the URI (e.g: my URI is 047616383171.dkr.ecr.us-east-2.amazonaws.com/mlproject)

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


	- Write docker --version to check whether Docker is working properly or not.
	
# 6. Configure EC2 as self-hosted runner:

    - Open and connect to your GitHub page.
    - Go to Settings > Actions > Runners > New self-hosted runner.
    - Select Runner image: Linux.
    - Run the commands from the "Download and Configure" section one by one in the terminal of the EC2 machine to connect GitHub to the EC2 instance.

# 7. Setup github secrets:

    - Click on Secrets and variables in Actions, then click on Actions.
    - Add a New repository secret and enter the required secrets.
    - The New repository secret names are:
      - AWS_ACCESS_KEY_ID
      - AWS_SECRET_ACCESS_KEY
      - AWS_REGION
      - AWS_ECR_LOGIN_URI
      - ECR_REPOSITORY_NAME
