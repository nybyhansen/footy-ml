from dataclasses import dataclass

import pandas as pd


@dataclass
class MLDataset:
    target_name: str
    feature_names: list[str]
    raw_data: pd.DataFrame

    @property
    def features(self) -> pd.DataFrame:
        if not set(self.feature_names) <= set(self.raw_data.columns.tolist()):
            raise KeyError("The given list of feature names is not existing in the raw data!")
        return self.raw_data[self.feature_names + ["fold"]]

    @property
    def target(self) -> pd.DataFrame:
        if not self.target_name in self.raw_data.columns.tolist():  # noqa
            raise KeyError(f"The target '{self.target_name}' was not present in the raw data!")
        return self.raw_data[self.target_name]
