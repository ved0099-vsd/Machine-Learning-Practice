from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    Data = {
        "Hours": [1,2,3,4,5,6,7,8,9,10],
        "Marks": [30,35,40,45,50,55,60,65,80,60]
    }

    df = pd.DataFrame(Data)

    X = df[["Hours"]]
    Y = df["Marks"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
#X — input features (study hours).
#y — target values (marks).
#test_size=0.2 — reserves 20% of the data for testing.
#random_state=42 — makes the random split reproducible, so you get the same split when you run it again with the same data and settings.

    print("Training Features : ")
    print(X_train)

    print("Testing Features:")
    print(X_test)

    print("Training targets")
    print(Y_train)

    print("Testing Targets")
    print(Y_test)

if __name__ == "__main__":
    main()