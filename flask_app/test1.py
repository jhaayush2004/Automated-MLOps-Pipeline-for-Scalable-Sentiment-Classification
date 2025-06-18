import mlflow
import os

# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/jhaayush2004/Automated-MLOps-Pipeline-for-Scalable-Sentiment-Classification.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "jhaayush2004"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "896e20aa99abc119ca1ac717c4163783eba40895"

# model = mlflow.pyfunc.load_model("models:/my_model/4")
# print("Model loaded successfully")


# from mlflow.artifacts import list_artifacts
# import os

# os.environ["MLFLOW_TRACKING_USERNAME"] = "jhaayush2004"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "896e20aa99abc119ca1ac717c4163783eba40895"

# mlflow.set_tracking_uri("https://dagshub.com/jhaayush2004/Automated-MLOps-Pipeline-for-Scalable-Sentiment-Classification.mlflow")

# print(list_artifacts(artifact_uri="models:/my_model/4"))

# import mlflow
# import mlflow.sklearn

# mlflow.set_tracking_uri("https://dagshub.com/jhaayush2004/Automated-MLOps-Pipeline-for-Scalable-Sentiment-Classification.mlflow")
# mlflow.set_experiment("sentiment-experiment")

# with mlflow.start_run() as run:
#     import joblib
#     from sklearn.linear_model import LogisticRegression
#     model = LogisticRegression().fit([[0, 1], [1, 1]], [0, 1])
    
#     # Log model properly under a registered model name
#     mlflow.sklearn.log_model(model, "model", registered_model_name="my_model")

# from mlflow.artifacts import list_artifacts
# print(list_artifacts("models:/my_model/5"))
# import os, mlflow
# os.environ["MLFLOW_TRACKING_USERNAME"] = "jhaayush2004"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "896e20aa99abc119ca1ac717c4163783eba40895"

# mlflow.set_tracking_uri("https://dagshub.com/jhaayush2004/Automated-MLOps-Pipeline-for-Scalable-Sentiment-Classification.mlflow")

# # List all experiments
# experiments = mlflow.search_experiments()
# print([exp.name for exp in experiments])
# mlflow.set_experiment("sentiment-experiment")

# with mlflow.start_run():
#     mlflow.log_metric("dummy", 1)
# mlflow.sklearn.log_model(, artifact_path="model", registered_model_name="my_model")
from mlflow.artifacts import list_artifacts
print(list_artifacts("models:/my_model/3"))