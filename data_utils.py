import kagglehub
import pandas as pd

def download_data():
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
    return path

def read_data(path):
    return pd.read_csv(path + "/creditcard.csv")