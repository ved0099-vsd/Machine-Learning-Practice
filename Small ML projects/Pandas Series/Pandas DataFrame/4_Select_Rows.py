import pandas as pd

Data = {
    "Name":["Ved","Soumya","Adi"], #Dict
    "Age":[22,23,22],
    "Marks":[99,89,69]
}

df = pd.DataFrame(Data)

print(df)

print("-" * 40)

print(df.head())

print("-" * 40)

print(df.shape)

print("-" * 40)

print(df.columns)

print("-" * 40)

print(df.info())

print("-" * 40)

print(df["Name"])

print("-" * 40)

print(df["Marks"])

print("-" * 40)

print(df[["Name", "Marks"]])

print("-" * 40)

print(df.iloc[0])

print("-" * 40)

print(df.iloc[1])

print("-" * 40)

print(df.iloc[0:2])

