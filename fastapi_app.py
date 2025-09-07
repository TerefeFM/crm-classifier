from fastapi import FastAPI
import pyspark
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.sql import SparkSession

app = FastAPI()

# Initialize Spark
spark = SparkSession.builder.appName("CRMClassifierAPI").getOrCreate()

# Load saved model (placeholder path)
model = RandomForestClassificationModel.load("models/crm_rf_model")

@app.get("/")
def root():
    return {"message": "CRM Classifier API is running!"}
