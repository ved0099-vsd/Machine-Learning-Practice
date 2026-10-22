import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Marks": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    }

    df = pd.DataFrame(data)

    X = df[["Hours"]]
    Y = df["Marks"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    print("Training Features")
    print(X_train)

    print("Testing Features")
    print(X_test)

    print("Training Targets")
    print(Y_train)

    print("Testing Targets")
    print(Y_test)
    
if __name__ == "__main__":
    main()