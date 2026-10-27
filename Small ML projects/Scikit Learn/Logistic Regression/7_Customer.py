from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Number of Store Visits
    X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

    # 0 = Did Not Buy, 1 = Bought
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_customers = [[2], [6], [9]]

    prediction = model.predict(new_customers)

    print("Predicted Results are :",prediction)
    

if __name__ == "__main__":
    main()