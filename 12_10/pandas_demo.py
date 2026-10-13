import pandas as pd
data = "data.csv"
names = 'james'
dataset = pd.read_csv(data)
datasetFind = dataset[dataset[names] == names]

print(datasetFind)