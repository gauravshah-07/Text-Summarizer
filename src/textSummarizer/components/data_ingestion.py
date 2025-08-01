import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name,headers = request.urlretrieve(
                url=self.config.sourrce_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {file_name} with following headers: {headers}")
        else:
            logger.info(f"File already exists at: {Path(self.config.local_data_file)}")
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)