from sklearn.linear_model import LogisticRegression
def main():
        # Feature: Number of Complaints
    X = [[0], [1], [2], [3], [4],
         [5], [6], [7], [8], [9]]

    # 0 = Stays, 1 = Leaves
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_customers = [[1], [5], [8]]

    prediction = model.predict(new_customers)

    print("Predicted Results are :",prediction)

if __name__ == "__main__":
    main()