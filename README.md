# 🏦 CRM Classifier with PySpark

This project is a **Compliance Risk Management (CRM) Classifier** built using **PySpark**.  
It demonstrates an end-to-end machine learning pipeline — from data ingestion to model training and evaluation — designed as a **capstone project** based on my CodeSignal PySpark learning path.

---

## 🚀 Project Overview
- **Goal:** Classify taxpayers into **Low, Medium, High** risk categories.  
- **Framework:** PySpark (RDD → DataFrames → MLlib).  
- **Approach:** End-to-end pipeline covering ingestion, preprocessing, feature engineering, model training, and evaluation.  
- **Context:** Inspired by real-world **Compliance Risk Management** use cases.

---

## 📂 Repository Structure

```plaintext
crm-classifier/
│
├── notebooks/              # Jupyter notebooks (step by step)
│   ├── 01_data_ingestion.ipynb
│   ├── 02_preprocessing_rdd_df.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_classification_models.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_deployment_demo.ipynb
│
├── data/                   # Sample / synthetic datasets
├── src/                    # Utility scripts (ETL, feature engineering, helpers)
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## 🛠️ Tech Stack

* Python 3.11
* PySpark 3.x
* MLlib (machine learning)
* scikit-learn (evaluation support)
* JupyterLab / VS Code

---

## 📖 Lessons Learned

* Practical use of **RDD transformations** and **DataFrames**.
* How to use **MLlib Pipelines** for reproducible workflows.
* Tradeoffs between **mini-batch vs. full dataset training**.
* Persisting trained models for reuse.

---

## 🎯 Future Work

* Add **MLflow** for experiment tracking.
* Try **ensemble models** for better accuracy.
* Deploy with **FastAPI** + Spark backend.
* Test with larger CRM-like datasets.

---

## 🙌 Acknowledgements

This project was built as a **capstone** to summarize my CodeSignal PySpark journey,
and inspired by compliance risk management research for the Ministry of Revenue.
Big thanks to the **CodeSignal Community** for making learning engaging and gamified. 🎉

```

✅ This copy has no duplicates, no unclosed code fences, and consistent formatting.  

Do you want me to also add a **“Getting Started” section** (installation + how to run notebooks) so others can clone and test it easily?
```
