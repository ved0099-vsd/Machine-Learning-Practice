from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    X = [[2], [4], [6], [8], [10],
     [12], [14], [16], [18], [20]]

    y = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

    X_train,X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    prediction = model.predict(X_test)

    print("Actual Results",y_test)
    print("Predicted Resultx",prediction)    

if __name__ == "__main__":
    main()