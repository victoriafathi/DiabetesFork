import mlflow
import os
from mlflow import log_metric, log_params, log_artifacts
from os.path import dirname, abspath, join
from yaml import safe_load

def main():
    dir = dirname(abspath(__file__))
    config_file = join(dir, 'config.yaml')

    with open(config_file, "r") as ymlfile:
        cfg = safe_load(ymlfile)
    
    # Configure mlflow
    mlflow.set_tracking_uri(cfg["mlflow_uri"])
    os.environ["MLFLOW_TRACKING_USERNAME"] = cfg["mlflow_user"]
    os.environ["MLFLOW_TRACKING_PASSWORD"] = cfg["mlflow_pass"]
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = cfg["mlflow_artifact_uri"]
    os.environ["AWS_ACCESS_KEY_ID"] = cfg["mlflow_artifact_user"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = cfg["mlflow_artifact_pass"]
    mlflow.set_experiment(cfg["mlflow_experiment"])

    log_metric("hello world", 0)    
    print("Hello World")

if __name__ == "__main__":
    main()
