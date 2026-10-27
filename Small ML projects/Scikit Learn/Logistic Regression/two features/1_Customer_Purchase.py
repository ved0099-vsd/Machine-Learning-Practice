from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Store Visits, Monthly Income in Thousands]
    X = [
        [1, 10],
        [2, 15],
        [2, 20],
        [3, 25],
        [4, 30],
        [5, 35],
        [6, 40],
        [7, 50]
    ]

    # 0 = Not Purchased, 1 = Purchased
    y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create model
    model = LogisticRegression()

    # Train model
    model.fit(X,y)

    # predict for new customers
    # store visits, monthly income in Thouusands

    new_customers = [
        [2, 18],
        [4, 30],
        [7, 45]
    ]

    pred = model.predict(new_customers)

    print("Customer Data: ", new_customers)
    print("Purchase Prediction: ", pred)

if __name__ == "__main__":
    main()