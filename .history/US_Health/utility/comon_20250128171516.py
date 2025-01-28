import os 
from pathlib import Path
from US_Health import logging

def create_folder(path):
    os.makedirs(path,exist_ok=True)
    logging.info()