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
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
        
        # if the model name already exists, raise an error
        if os.path.exists(self.config.root_dir + "/" + self.config.model_name):   
            raise FileExistsError(f"The model file {self.config.model_name} already exists, choose a different name")

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))