# data_loader.py
import pandas as pd

def load_data():
    url = "https://drive.google.com/uc?id=1N6P2DslDuTBPqe8njbI6G67iqJF5hUpG"
    df = pd.read_csv(url)
    df["Date Joined"] = pd.to_datetime(df["Date Joined"], errors="coerce")
    df["Year"] = df["Date Joined"].dt.year
    return df
