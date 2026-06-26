import joblib 
import pandas as pd
from pathlib import Path
import numpy as np
from mlProject.entity.config_entity import PredictionNewDataConfig

# Ajouter méthode de noramlisation, PCA etc si vous avez en training
class PredictionNewDataPipeline:
    def __init__(self, config: PredictionNewDataConfig):
        self.config = config

        
    def Normalize_input_data(self, input_data):
        
        df_transf_data = pd.read_csv(self.config.transf_data_file)
        
        encoder =  joblib.load(self.config.encoder_file)
        
        str_values = [x for x in input_data if isinstance(x, str)]

        encoded_str_values = []

        for value, col in zip(str_values, self.config.column_str_name):
            encoded_value = encoder[col].transform([value])[0]
            encoded_str_values.append(encoded_value)

        # remplaer str dans input data par [1, 0, 0, 0, 1, 1, 0]
        # Récupérer les indices des valeurs string
        string_indices = [i for i, value in enumerate(input_data) if isinstance(value, str)]

        # Remplacer chaque valeur string par la valeur correspondante du mapping
        for idx, map_val in zip(string_indices, encoded_str_values):
            input_data[idx] = map_val

        input_normalized_data = (input_data - df_transf_data ["mean_input_data"]) / (df_transf_data ["max_input_data"] - df_transf_data ["min_input_data"])
        
        return input_normalized_data
    
    def predict(self, input_normalized_data):
        model = joblib.load(self.config.model_path)
        prediction = model.predict(np.array(input_normalized_data).reshape(1, 12))

        return prediction