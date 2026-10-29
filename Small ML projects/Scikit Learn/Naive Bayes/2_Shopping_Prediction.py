from sklearn.naive_bayes import GaussianNB

def main():
    # Feature: Time spent on website (minutes)
    X = [[2], [5], [8], [10], [15], [20], [25], [30]]

    # 0 = Will Not Buy, 1 = Will Buy
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()
    model.fit(X,y)

    new_visitors = [[6], [18], [28]]

    prediction = model.predict(new_visitors)

    print("Time Spent: ", new_visitors)

    print("Purchase Predictions :", prediction)


if __name__ == "__main__":
    main()