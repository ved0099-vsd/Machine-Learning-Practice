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

#Step 2 : Data Analysis(EDA)

print(Border)
print("Step 2 : Data Analysis(EDA)")
print(Border)

print("Shape of Dataset :",df.shape)
#df.shape returns the number of rows and columns.

print("Column Names :",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum())
#df.isnull() checks each cell for a missing value.
#.sum() counts the missing values in each column because True counts as 1.

print("Class distribution (Species count) :")
print(df["species"].value_counts())
#.value_counts() counts how many times each species appears.

print("Statistical report of Dataset :")
print(df.describe())
#df.describe() calculates summary statistics for numeric columns.

# Step 3 : Decide Independent and Dependent Variables

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X = Independent Variable/Features
# Y = Dependent Variables/Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal lenght (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
#df[feature_cols] selects only the four specified columns.
#X stores those selected columns.

Y = df["species"]

print("X shape :",X.shape)
print("Y Shape :",Y.shape)
