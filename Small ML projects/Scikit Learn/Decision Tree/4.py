from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[10], [20], [30], [40], [50], [60]]
    Y = [0, 0, 0, 1, 1, 1]

    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(X,Y)

    prediction = Model.predict([[10],[40],[60]])
    print("Model Predicted",prediction)

if __name__ == "__main__":
    main()