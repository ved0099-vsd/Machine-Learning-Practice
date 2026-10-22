from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[1], [2], [3], [4], [5], [6]]
    y = [0, 0, 1, 1, 2, 2]

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X,y)

    prediction = model.predict([[2], [3], [5]])
    print(prediction)

if __name__ == "__main__":
    main()