import pandas as pd
#pandas (pd) — loads and handles tabular data.

import matplotlib.pyplot as plt
#matplotlib.pyplot (plt) — creates graphs and charts.

import seaborn as sns
#- seaborn (sns) — provides additional statistical visualization tools.

from sklearn.model_selection import train_test_split
#sklearn is the Scikit-learn machine learning library.
#model_selection contains tools for preparing and evaluating models.
#- train_test_split divides your dataset into training and testing portions.

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report
)

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

# Step 4 : Visualization Of DataSet

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5)) #(Width,height in inches)
#This creates a figure for your graph.

for sp in df["species"].unique():
#.unique() returns the distinct species names.

    temp = df[df['species'] == sp ]
    #This selects only the rows belonging to the current species.

    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)
    #temp["petal length (cm)"] → X-axis values.
    #temp["petal width (cm)"] → Y-axis values.
    #- label=sp → assigns the species name to that group of points.

plt.title("Iris Case Study")

plt.xlabel("Petal lenght (cm)")
plt.ylabel("Petal width (cm)")

plt.legend() #Display
plt.grid()  #grid lines
plt.show()  #opens and displays the completed plot


#Step 5 : Split the dataset for training and testing

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5, random_state = 42)
#Variable	Meaning
#X_train	Features used to train the model
#X_test	Features used to test the model
#Y_train	Correct labels used during training
#Y_test	Correct labels used to evaluate predictions

#Test_size 0.5 = It means 50% of the dataset is used for testing and the remaining 50% for training.

print("Dataset splitting activity done")

print("X:",X.shape)
print("Y_test :",Y.shape)

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)

print("Y_train :",Y_train.shape)
print("Y_test :", Y_test.shape)

#Step 6 : Build the model

print(Border)
print("Step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)
#DecisionTreeClassifier() creates a classification model.
#max_depth=5 limits the tree's maximum depth to 5 levels.

print("Model gets created successfully")

#Step 7 : Train the Model

print(Border)
print("step 7 : Train the Model")
print(Border)

model.fit(X_train, Y_train)
print("Model trained successfully")

#model → your Decision Tree Classifier.
#fit() → trains the model.
#X_train → flower measurements (input features).
#Y_train → correct flower species (target labels).

#Step 8 : Evaluate the Model

print(Border)
print("Step 8: Evaluate the Model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Evaluating Done")

print("Expected ANS print :")
print(Y_test)

print("Predicted ans:")
print(Y_pred)

#Step 9: Evaluate the model Performance

print(Border)
print("Step 9 : Evaluate the Model Performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of model is ",accuracy*100)

print("Confusion Matrix")
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

print("Classification report")
print(classification_report(Y_test, Y_pred))