import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "Performance": [25, 30, 38, 45, 52, 60, 65, 72, 78, 85, 90, 98]
    }

    df = pd.DataFrame(Data)

    X = df[["StudyHours"]]
    Y = df["Performance"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42, test_size=0.2)

    print("Training Features: ")
    print(X_train)

    print("testing Features")
    print(X_test)

    print("training Inputs")
    print(Y_train)

    print("testing inputs")
    print(Y_test)


if __name__ == "__main__":
    main()