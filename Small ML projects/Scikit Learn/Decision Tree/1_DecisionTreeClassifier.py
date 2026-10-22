from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[1], [1], [2], [2], [3], [3]]
    Y = [10, 10, 20, 20, 30, 30]

    model = DecisionTreeClassifier(random_state=42)
#model = DecisionTreeClassifier(...) — create the model.

    model.fit(X, Y)
#model.fit(X, y) — train the model.

    prediction = model.predict([[1],[2],[3]])
#model.predict([[1], [2], [3]]) — predict classes for three inputs.

    print("Predicted Classes :", prediction)

if __name__ == "__main__":
    main()
