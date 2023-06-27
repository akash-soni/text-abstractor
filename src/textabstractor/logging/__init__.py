import logging
import os
from datetime import datetime
import sys

# creating a log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log file path
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    # filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("textAbstractorLogger")
