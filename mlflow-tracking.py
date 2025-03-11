import mlflow

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://host.docker.internal:5001")  # noqa: E501, W292