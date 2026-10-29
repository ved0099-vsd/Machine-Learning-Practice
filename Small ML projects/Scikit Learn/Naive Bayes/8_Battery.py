from sklearn.naive_bayes import GaussianNB

def main():
    # battery Percentage
    X = [[20], [30], [40], [45], [75], [80], [90], [95]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_percentage = [[35], [65], [90]]

    pred = model.predict(new_percentage)

    print("New Data = ", new_percentage)

    print("Predicted Results :", pred)

if __name__ == "__main__":
    main()