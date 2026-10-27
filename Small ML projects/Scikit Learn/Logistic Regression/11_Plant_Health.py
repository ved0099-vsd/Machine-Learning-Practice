from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Number of Yellow Leaves
    X = [[0], [1], [2], [3], [4],
         [5], [6], [7], [8], [9]]

    # 0 = Healthy, 1 = Unhealthy
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_plants = [[1], [5], [8]]

    prediction = model.predict(new_plants)

    print("New Predictions :",prediction)

if __name__ == "__main__":
    main()