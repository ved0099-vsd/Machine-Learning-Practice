import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "Temperature": [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
        "IceCreamSales": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    }

    df = pd.DataFrame(Data)

    X = df[["Temperature"]]
    Y = df["IceCreamSales"]

    X_train, X_test, Y_Train, Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Training features")
    print(X_train)

    print("Testing Features")
    print(X_train)

    print("training inputs")
    print(Y_Train)

    print("testing inputs")
    print(Y_test)

if __name__ == "__main__":
    main()