import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data_normalized = None  # Initialiser comme None
        
    
    ## Note: You can add other data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    def Normalize_data (self):
        
        data = pd.read_csv(self.config.data_path)
        
        input_data = data.drop(self.config.all_schema.TARGET_COLUMN.name, axis=1)
        
         # get mean, max and min values of the input data
        mean_input_data, max_input_data, min_input_data = input_data.mean(), input_data.max(), input_data.min()

        # normalize les donné d'entré avec la normalisation moyenne 
        input_normalized_data = (input_data - mean_input_data)/(max_input_data-min_input_data)

        # Concate target (output) to input normalised_data
        self.data_normalized = pd.concat([input_normalized_data , data[self.config.all_schema.TARGET_COLUMN.name]], axis=1)

        return self.data_normalized
        
        
    def train_test_splitting(self, data_normalized):
  
       # Split the input normalized data into training, validation and test sets : (0.70, 0.15, 0.15)
        train, test_val = train_test_split(data_normalized, test_size=0.30, random_state=42)
        validation, test = train_test_split(test_val, test_size=0.50, random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        validation.to_csv(os.path.join(self.config.root_dir, "validation.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Split data into training, validation and test sets")
        logger.info("train shape: " + str(train.shape))
        logger.info("validation shape: " + str(validation.shape) )      
        logger.info("test shape: "+ str(test.shape))