from sklearn.tree import DecisionTreeClassifier

def main():
    X = [[10], [20], [30], [40], [50], [60]]
    y = [0, 0, 1, 1, 2, 2]

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X,y)

    prediction = model.predict([[10], [30], [50], [60]])
    print(prediction)
    
if __name__ == "__main__":
    main()