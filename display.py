import pandas as pd

df = pd.read_csv('processed.csv')
rowNum = len(df)
print(rowNum)
for i in range(rowNum):
    print(list(df.loc[i]))
