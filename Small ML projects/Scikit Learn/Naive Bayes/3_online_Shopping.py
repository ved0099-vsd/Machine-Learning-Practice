from sklearn.naive_bayes import GaussianNB

def main():
    # time spent
    X = [[2], [5], [8], [10], [15], [20], [25], [30]]

#    0 = wont buy, 1 = will buy
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_customers = [[6], [18], [28]]

    prediction = model.predict(new_customers)

    print("new customers are :", new_customers)
    print("Prediction Results are :", prediction)

if __name__ == "__main__":
    main()