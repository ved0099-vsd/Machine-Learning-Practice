from sklearn.naive_bayes import GaussianNB

def main():
    # Daily Steps
    X = [[1000], [2000], [3000], [4000], [7000], [8000], [9000], [10000]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_Data = [[2500], [6000], [9500]]

    pred = model.predict(new_Data)

    print("New data is :", new_Data)

    print("Prediction is :", pred)

if __name__ == "__main__":
    main()