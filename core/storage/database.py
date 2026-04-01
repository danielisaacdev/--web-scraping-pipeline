from abc import ABC, abstractmethod
import pandas as pd
from core.monitoring.logger import setup_logger

class StorageProvider(ABC):
    @abstractmethod
    def save(self, data: any, destination: str):
        pass

class CSVStorage(StorageProvider):
    def __init__(self):
        self.logger = setup_logger("CSVStorage")

    def save(self, data: pd.DataFrame, destination: str):
        try:
            data.to_csv(destination, index=False, sep=";", encoding="utf-8-sig", quoting=1)
            self.logger.info(f"Data successfully saved to {destination}")
        except Exception as e:
            self.logger.error(f"Error saving CSV: {e}")

class DatabaseStorage(StorageProvider):
    # Esto sería para PostgreSQL/Elasticsearch
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def save(self, data: any, destination: str):
        # Implementar lógica de SQLAlchemy o PyMongo aquí
        pass
