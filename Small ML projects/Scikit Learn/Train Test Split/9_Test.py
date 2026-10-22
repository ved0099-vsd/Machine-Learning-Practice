import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "PracticeTests": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "FinalMarks": [30, 35, 42, 48, 55, 60, 65, 70, 76, 82, 88, 95]
    }

    df = pd.DataFrame(Data)

    X = df[["PracticeTests"]]
    Y = df["FinalMarks"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

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