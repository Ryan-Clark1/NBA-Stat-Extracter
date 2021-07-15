import os
import pandas as pd
import openpyxl

#file_list = []
#for file in os.listdir():
#    if file.endswith('_basic.csv'):
#        df = pd.read_csv(file,sep=";")
#        file_list.append(df)

#all_days = pd.concat(file_list, ignore_index=True)
#all_days.to_csv("master_MASTER_basic_database.csv")

file_list = []
for file in os.listdir():
    if file.endswith('_advanced.csv'):
        df = pd.read_csv(file,sep=";")
        file_list.append(df)

all_days = pd.concat(file_list, ignore_index=True)
all_days.to_csv("master_MASTER_advanced_database.csv")

#file_list = []
#for file in os.listdir():
#    if file.endswith('_game_record.csv'):
#        df = pd.read_csv(file,sep=";")
#        file_list.append(df)

#all_days = pd.concat(file_list, ignore_index=True)
#all_days.to_csv("MASTER_game_record_Database.csv")

#file_list = []
#for file in os.listdir():
#    if file.endswith('_game_record.csv') or file.endswith('advanced.csv') or file.endswith('basic.csv'):
#        os.remove(file)