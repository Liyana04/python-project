import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Financial Sample.xlsx"
df = pd.read_excel(excel_file_path)
print(df)
