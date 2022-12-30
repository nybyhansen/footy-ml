from abc import ABC, abstractmethod

import pandas as pd


class IPredictiveModel(ABC):
    @abstractmethod
    def fit(self, features: pd.DataFrame, target: pd.Series) -> None:
        ...

    @abstractmethod
    def predict(self, features: pd.DataFrame) -> pd.Series:
        ...
