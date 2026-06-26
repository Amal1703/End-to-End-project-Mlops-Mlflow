import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        
        train_data = pd.read_csv(self.config.train_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)

        train_y = train_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
        
        # if the model name already exists, add 1 to the model name to have a new model name 
        model_name = self.config.model_name 
        base_name, extension = os.path.splitext(model_name)
        
        counter = 1
        new_name = model_name

        while os.path.exists(os.path.join(self.config.root_dir, new_name)):
            new_name = f"{base_name}{counter}{extension}"
            counter += 1

        joblib.dump(lr, os.path.join(self.config.root_dir, new_name))