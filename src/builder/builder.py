from src.builder.dataset import MLDataset
from src.builder.models import IPredictiveModel
from src.builder.registry import IModelRegistry


class Builder:
    def __init__(
        self, dataset: MLDataset, registry: IModelRegistry, feature_names: list[str]
    ) -> None:
        self._dataset = dataset
        self._registry = registry
        self._feature_names = feature_names

        def build(self, model: IPredictiveModel) -> None:
            raise NotImplementedError()
