from pydantic import BaseSettings


class GlobalSettings(BaseSettings):
    TRAINING_DATA_ENDPOINT: str = "https://api.footy-tracker.live/ml/training_data/json"


def get_settings():
    return GlobalSettings()


settings = get_settings()
