from abc import ABC, abstractmethod

from src.builder.models import IPredictiveModel


class IModelRegistry(ABC):
    @abstractmethod
    def log_model(self, model: IPredictiveModel) -> None:
        ...


class FakeModelRegistry(IModelRegistry):
    def log_model(self, model: IPredictiveModel) -> None:
        print("Model logged! Fake news..")
