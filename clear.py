import os
import pandas as pd
import openpyxl

file_list = []
for file in os.listdir():
    if file.endswith('_game_record.csv') or file.endswith('advanced.csv') or file.endswith('basic.csv'):
        os.remove(file)
