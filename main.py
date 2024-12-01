import pandas as pd

df = pd.read_csv('2011washington.csv')

print(df.head())
print(df.info())
print(df.describe())
