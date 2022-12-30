import pandas as pd


def create_validation_folds(dataset: pd.DataFrame, n_last_records: int) -> pd.DataFrame:
    """Validation scheme function that adds a new columns indicating the train/test split."""
    result_id_ordered = dataset.sort_values("result_dt").result_id.tolist()

    train_result_id = result_id_ordered[:n_last_records]
    test_result_id = result_id_ordered[n_last_records:]

    train_mask = dataset.result_id.isin(train_result_id)
    test_mask = dataset.result_id.isin(test_result_id)

    dataset.loc[train_mask, "fold"] = "train"
    dataset.loc[test_mask, "fold"] = "test"

    return dataset
