from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[1], [2], [3], [4], [5], [6]] #Study hours
    Y = [[0], [0], [0], [1], [1], [1]] # Result category 0 = fail 1 = pass

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X,Y)

    prediction = model.predict([[2],[5]])

    print("Model Predicted",prediction)



if __name__ == "__main__":
    main()