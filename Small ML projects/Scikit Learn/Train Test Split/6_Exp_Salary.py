import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "Salary": [15000, 18000, 22000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]
    }

    df = pd.DataFrame(Data)

    X = df[["Experience"]]
    Y = df["Salary"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    print("training features")
    print(X_train)

    print("testing features")
    print(X_train)

    print("Training inputs")
    print(Y_train)

    print("Testing inputs")
    print(Y_test)



if __name__ == "__main__":
    main()