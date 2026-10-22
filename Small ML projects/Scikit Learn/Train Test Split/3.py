import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Marks": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    }

    df = pd.DataFrame(Data)

    X = df[["Hours"]]
    Y = df["Marks"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Training Features ")
    print(X_train)

    print("Testing Features")
    print(X_train)

    print("Training Input")
    print(X_train)

    print("Testing Input")
    print(Y_test)


if __name__ == "__main__":
    main()