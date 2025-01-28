import os 
from pathlib import Path
from US_Health import logging
import dill

def create_folder(path):
    os.makedirs(path,exist_ok=True)
    logging.info(f"{path}folder create successfully")
    
def save_object(file_path: str, obj: object) -> None:

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise e    