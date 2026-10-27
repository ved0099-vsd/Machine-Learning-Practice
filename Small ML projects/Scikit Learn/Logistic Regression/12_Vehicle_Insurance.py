from sklearn.linear_model import LogisticRegression

def main():
        # Feature: Vehicle Age in Years
    X = [[1], [2], [3], [4], [5],
         [6], [7], [8], [9], [10]]

    # 0 = Not Purchased, 1 = Purchased
    y = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

    model = LogisticRegression()

    model.fit(X,y)

    new_vehicles = [[2], [6], [9]]

    prediction = model.predict(new_vehicles)

    print("Prediction results are :", prediction)

if __name__ == "__main__":
    main()