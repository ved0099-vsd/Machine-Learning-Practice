from sklearn.naive_bayes import GaussianNB

def main():
    # mileage
    X = [[5], [7], [9], [10], [15], [18], [20], [25]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_data = [[8], [13], [22]]

    pred = model.predict(new_data)

    print("New Data is :", new_data)

    print("Predicted Results are :", pred)

if __name__ == "__main__":
    main()