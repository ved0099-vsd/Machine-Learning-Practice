import pandas as pd

Data = {
    "Name" : ["Amit", "Rahul","Sneha","Priya","Ved"],
    "Age" : [21,22,None,23,21],
    "Marks" : [85,None, 91,68,88],
    "City": ["Pune", "Mumbai", "Pune", None, "Pune"]
}

df = pd.DataFrame(Data)
print(df)

Border = "-" * 40
print(Border)

print("1.Count missing values in each column using `isnull().sum()`.")
print(df.isnull().sum())

print(Border)

print("2.Display the DataFrame after removing rows containing missing values using `dropna")
print(df.dropna())

print(Border)

print("3.Fill missing Marks with 0 using `fillna()`.")
print(df["Marks"].fillna(0))

print(Border)

print("4.Display summary statistics for numeric columns using `describe()`.")
print(df.describe())

print(Border)

print("5.Calculate the average Marks, ignoring missing values.")
print(df["Marks"].mean())