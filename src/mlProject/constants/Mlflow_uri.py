import dagshub 

# Initialize DagsHub and connect MLflow tracking to the specified repository
dagshub.init(repo_owner='kamounamal34', repo_name='End-to-End-project-Mlops-Mlflow', mlflow=True) 


Mlflow_Tracking_uri = "https://dagshub.com/kamounamal34/End-to-End-project-Mlops-Mlflow.mlflow"


experiment_name = "Price_house_pred" # define the experiment name (in Mlflow)