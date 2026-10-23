from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]] # Hours Practiced
    y = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2] # Skill category

    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.2)
    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)
    prediction = model.predict(X_test)

    print("Actual Prediction",y_test)
    print("Predicted results ",prediction)


if __name__ == "__main__":
    main()