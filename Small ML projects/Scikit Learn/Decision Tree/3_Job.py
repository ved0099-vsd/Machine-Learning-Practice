from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[1],[2],[3],[4],[5],[6]]
    y = [0, 0, 1, 1, 2, 2]
    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(X,y)
    prediction = Model.predict([[1],[4],[6]])
    print("Model Predicted using Decisiontree classifier",prediction)



if __name__ == "__main__":
    main()