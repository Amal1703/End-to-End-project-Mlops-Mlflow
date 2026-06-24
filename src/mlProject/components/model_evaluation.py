import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import numpy as np
import joblib
from mlProject.constants import *
from mlProject.utils.common import read_yaml
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path
from mlProject.constants.Mlflow_uri import experiment_name
import glob

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        params_filepath = PARAMS_FILE_PATH
        self.params = read_yaml(params_filepath)
        

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        
        #model = joblib.load(self.config.model_path)
        
       # Charger le model le plus récent
        model_dir = self.config.model_path

        latest_model = max(
            glob.glob(os.path.join(model_dir, "*.joblib")),
            key=os.path.getmtime
        )

        model = joblib.load(latest_model)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        mlflow.set_experiment(experiment_name) # define the experiment name
        
        with mlflow.start_run(run_name = (self.params.Model_name +  "_model") ):

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            

        # if the metric file name  already exists, add 1 to the metric file name to have a new metric file name 
            metric_file_name = self.config.metric_file_name  # ex: metrics.json
            base_name, extension = os.path.splitext(metric_file_name)

            counter = 1
            new_metric_file_name = metric_file_name

            while os.path.exists(new_metric_file_name):
                new_metric_file_name = f"{base_name}{counter}{extension}"
                counter += 1

            save_json(path=Path(new_metric_file_name), data={**scores, 
                                                             "loaded_model_params": str(model),
                                                            "loaded_model_path": str(Path(latest_model).as_posix()) })


            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            
            # If I am connected to an MLflow server (DagsHub) => register the model
            if tracking_url_type_store != "file":

                # Register the model
                mlflow.sklearn.log_model(sk_model=model, artifact_path="model",registered_model_name = self.params.Model_name )

            # If I am working locally, save the model as a file          
            else:  
                mlflow.sklearn.log_model(sk_model=model, artifact_path="model",registered_model_name = self.params.Model_name)