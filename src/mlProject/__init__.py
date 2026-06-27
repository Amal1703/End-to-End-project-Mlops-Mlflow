import os
import sys
import logging

# asctime: The date and time when the log record was created
# levelname: log level (INFO, ERROR, etc.)
# module: name of the Python file that generated the log
# message: log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 


# define the path of the file that will contain the logs
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") 

# Create a folder "logs"
os.makedirs(log_dir, exist_ok=True) 


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[ 
        logging.FileHandler(log_filepath), # save log in the file "log_filepath"
        logging.StreamHandler(sys.stdout)  # print log in the terminal
    ]
)

# Create a logger with a specific name for your project
logger = logging.getLogger("mlProjectLogger")