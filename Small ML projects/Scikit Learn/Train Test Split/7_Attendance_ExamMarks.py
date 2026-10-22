import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
        "ExamMarks": [35, 40, 45, 55, 60, 70, 80, 95]
    }

    df = pd.DataFrame(Data)

    X = df[["Attendance"]]
    Y = df["ExamMarks"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

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