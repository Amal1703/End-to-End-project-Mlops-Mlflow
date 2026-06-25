import os
import joblib
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
        
    def train_test_splitting(self):
        
        data = pd.read_csv(self.config.data_path)
  
       # Split the input normalized data into training and test sets : (0.80, 0.20)
        train_data, test_data= train_test_split(data, test_size=0.20, random_state=42)
        
        logger.info("Split data into training and test sets")
        logger.info("train shape: " + str(train_data.shape))  
        logger.info("test shape: "+ str(test_data.shape))
        
        return train_data, test_data
    
    ## Note: You can add other data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    def Normalize_data (self, train_data, test_data):
        
       # data = pd.read_csv(self.config.data_path)
       
        # 1. Train data
        input_train_data = train_data.drop(self.config.all_schema.TARGET_COLUMN.name, axis=1)
        
         # Transform string input data to integer 

        column_name = ["mainroad", "guestroom", "basement", "hotwaterheating",
                       "airconditioning", "prefarea", "furnishingstatus"]

        encoders = {}

        for col in column_name:
            encoder = LabelEncoder()
            input_train_data[col] = encoder.fit_transform(input_train_data[col])  # Transform and replace directly
            encoders[col] = encoder
         
         # Save encoders
        joblib.dump(encoders, self.config.encoder_file)

         # get mean, max and min values of the input data
        mean_input_data, max_input_data, min_input_data = input_train_data.mean(), input_train_data.max(), input_train_data.min()
        
        # Save mean, max and min values of the input data (to normalize the new test data)
        transf_data = pd.DataFrame({
                 "mean_input_data": mean_input_data,
                "max_input_data": max_input_data,
                "min_input_data": min_input_data
                })

        transf_data.to_csv(self.config.transf_data_file)


        # normalize les donné d'entré avec la normalisation moyenne 
        input_normalized_train_data = (input_train_data - mean_input_data)/(max_input_data-min_input_data)

        # Concate target (output) to input normalised_data
        data_train_normalized = pd.concat([input_normalized_train_data , train_data[self.config.all_schema.TARGET_COLUMN.name]], axis=1)

        data_train_normalized.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        
        # 2. Test data
        input_test_data = test_data.drop(self.config.all_schema.TARGET_COLUMN.name, axis=1)
        
        for col in column_name:
            input_test_data[col] = encoders[col].transform(input_test_data[col])  # Transform and replace directly
        
        # normalize les donné d'entré avec la normalisation moyenne 
        input_normalized_test_data = (input_test_data - mean_input_data)/(max_input_data-min_input_data)

        # Concate target (output) to input normalised_data
        data_test_normalized = pd.concat([input_normalized_test_data , test_data[self.config.all_schema.TARGET_COLUMN.name]], axis=1)

        data_test_normalized.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
