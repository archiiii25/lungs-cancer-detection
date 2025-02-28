import dagshub
dagshub.init(repo_owner='ARYAN-DIXIT1', repo_name='lungs-cancer-detection', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)