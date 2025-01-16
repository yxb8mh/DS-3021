import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

df.to_csv("iris.csv", index=False)
print("Data saved to iris.csv")

