import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "SleepHours": [4, 5, 6, 7, 8, 9, 4, 6, 7, 8],
        "Productivity": [40, 45, 55, 65, 80, 90, 42, 58, 70, 85]
    }

    df = pd.DataFrame(Data)

    X = df[["SleepHours"]]
    Y = df["Productivity"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Training Features: ")
    print(X_test)

    print("testing Features")
    print(X_test)

    print("training Inputs")
    print(Y_train)

    print("testing inputs")
    print(Y_test)

if __name__ == "__main__":
    main()