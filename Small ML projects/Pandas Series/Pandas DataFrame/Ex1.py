import pandas as pd

Data = {
    "Name":["Ved","Sotu","Pappu"],
    "Age" :[22, 21,22],
    "Marks" : [87,98,87]
}

df = pd.DataFrame(Data)
print(df)

print("Shape:",df.shape)
print("-" * 30)
print(df["Marks"])
print("-" * 30)
print(df.iloc[2])
print("-" * 30)

print(df[df["Marks"] > 80])
print(df[df["Marks"] > 100])

print(df.sort_values("Marks", ascending=False))

