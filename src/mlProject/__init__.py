import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # levelname : Niveau du log (INFO, ERROR, etc.) , module : Nom du fichier Python qui a créé le log, message : message du log


log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") # Définit le chemin du fichier qui contiendra les log
os.makedirs(log_dir, exist_ok=True) # crée le dossier "logs"


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[ 
        logging.FileHandler(log_filepath), # save log in the file "log_filepath"
        logging.StreamHandler(sys.stdout)  # print log in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger") #  crée un logger avec un nom spécifique pour votre projet