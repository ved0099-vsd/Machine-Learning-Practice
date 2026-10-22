import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    Data = {
        "StudyHours": [2,3,4,5,6,7,8,9],
        "Scores" : [35,40,45,50,55,60,65,90]
    }

    df = pd.DataFrame(Data)

    X = df[["StudyHours"]]
    Y = df["Scores"]

    X_test,X_train,Y_test,Y_Test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("training Features")
    print(X_train)

    print("testing features")
    print(X_test)

    print("traininig inputs")
    print(Y_test)

    print("testing imputs")
    print(Y_test)

if __name__ == "__main__":
    main()