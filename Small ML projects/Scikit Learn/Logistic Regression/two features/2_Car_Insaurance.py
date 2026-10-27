from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Customer Age, Annual Income in Lakhs]
    X = [
        [20, 2],
        [25, 3],
        [30, 4],
        [35, 5],
        [40, 6],
        [45, 7],
        [50, 8],
        [55, 9]
    ]

    # 0 = Not Purchased, 1 = Purchased
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_customers = [
        [22, 2.5],
        [38, 5.5],
        [52, 8.5]
    ]

    pred = model.predict(new_customers)

    print("New customer data: ",new_customers)
    print("Predicted Results : ", pred)

if __name__ == "__main__":
    main()