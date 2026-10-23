from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

    y = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

    X_train,X_test, y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    prediction = model.predict(X_train,y_train)

    print("Actual Results",y_test)
    print("Presdicted Results", prediction)

if __name__ == "__main__":
    main()