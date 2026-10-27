from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Vehicle Age, Annual Kilometres in Thousands]
    X = [
        [1, 5], [2, 8], [3, 10], [4, 12],
        [5, 18], [6, 22], [7, 25], [8, 30]
    ]

    # 0 = Not Purchased, 1 = Purchased
    y = [1, 1, 1, 1, 0, 0, 0, 0]

    model = LogisticRegression()

    model.fit(X,y)

    new_vehicles = [[2,7], [17,20],[12,8],[67,54]]

    pred = model.predict(new_vehicles)

    print("New data: ", new_vehicles)

    print("Predicted results: ", pred)

if __name__ == "__main__":
    main()