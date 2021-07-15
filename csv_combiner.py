import os
import pandas as pd
import openpyxl

file_list = []
for file in os.listdir():
    if file.endswith('_advanced.csv'):
        df = pd.read_csv(file,sep=";")
        file_list.append(df)

all_days = pd.concat(file_list, ignore_index=True)
all_days.to_csv("master_MASTER_advanced_database.csv")

