import pandas as pd

Border = "-" * 40

#Step 1 : Load the data set

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"
#df = Data Frame
df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print("Initial entries from dataset are :")
print(df.head())