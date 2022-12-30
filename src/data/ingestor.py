from abc import ABC, abstractmethod

import pandas as pd
import requests

from src.config import settings


class IDataIngestor(ABC):
    @abstractmethod
    def get_historical_results(self) -> pd.DataFrame:
        ...


class DataIngestor(IDataIngestor):
    def get_historical_results(self) -> pd.DataFrame:
        response = requests.get(settings.TRAINING_DATA_ENDPOINT)
        if response.status_code == 200:
            return pd.DataFrame.from_dict(response.json().get("data"))
