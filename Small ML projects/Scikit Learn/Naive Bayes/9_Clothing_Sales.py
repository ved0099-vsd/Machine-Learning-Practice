from sklearn.naive_bayes import GaussianNB

def main():
    # Discount Percenatage
    X = [[0], [5], [10], [15], [30], [40], [50], [60]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_data = [[8], [25], [55]]

    pred = model.predict(new_data)

    print("New Data:", new_data)

    print("Predicted Results :", pred)

if __name__ == "__main__":
    main()