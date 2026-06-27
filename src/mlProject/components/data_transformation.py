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
  
       # split the data into training and test sets : (0.80, 0.20)
        train_data, test_data= train_test_split(data, test_size=0.20, random_state=42)
        
        logger.info("Split data into training and test sets")
        logger.info("train shape: " + str(train_data.shape))  
        logger.info("test shape: "+ str(test_data.shape))
        
        return train_data, test_data
    
    ## Note: You can add other data transformation techniques such as PCA 
    # You can perform all kinds of exploratory data analysis (EDA) here before passing the data to the model

    def Normalize_data (self, train_data, test_data):
        
        # column_name = ["mainroad", "guestroom", "basement", "hotwaterheating","airconditioning", "prefarea", "furnishingstatus"]
        column_name = self.config.column_str_name
             
        # 1. Train data
        input_train_data = train_data.drop(self.config.all_schema.TARGET_COLUMN.name, axis=1)
        
         # convert the training input data from strings to integer values
        encoders = {}

        for col in column_name:
            encoder = LabelEncoder()
            input_train_data[col] = encoder.fit_transform(input_train_data[col])  
            encoders[col] = encoder
         
         # save encoders
        joblib.dump(encoders, self.config.encoder_file)

         # get mean, max and min values of the training input data for normalizing new test data
        mean_input_data, max_input_data, min_input_data = input_train_data.mean(), input_train_data.max(), input_train_data.min()
        
        # save mean, max and min values of the training input data for normalizing new test data
        transf_data = pd.DataFrame({
                "mean_input_data": mean_input_data,
                "max_input_data": max_input_data,
                "min_input_data": min_input_data
                })

        transf_data.to_csv(self.config.transf_data_file)

        # normalize the training input data using mean normalization
        input_normalized_train_data = (input_train_data - mean_input_data)/(max_input_data-min_input_data)

        # concatenate the output data with the normalized training input data and save it
        data_train_normalized = pd.concat([input_normalized_train_data , train_data[self.config.all_schema.TARGET_COLUMN.name]], axis=1)
        data_train_normalized.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        
        # 2. Test data
        input_test_data = test_data.drop(self.config.all_schema.TARGET_COLUMN.name, axis=1)
        
        # convert the test input data from strings to integer values
        for col in column_name:
            input_test_data[col] = encoders[col].transform(input_test_data[col])  
        
        # normalize the test input data using mean normalization
        input_normalized_test_data = (input_test_data - mean_input_data)/(max_input_data-min_input_data)

        # concatenate the output data with the normalized test input data and save it
        data_test_normalized = pd.concat([input_normalized_test_data , test_data[self.config.all_schema.TARGET_COLUMN.name]], axis=1)
        data_test_normalized.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
