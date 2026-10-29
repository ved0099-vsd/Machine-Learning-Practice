from sklearn.naive_bayes import GaussianNB

def main():
    # price in Lakhs
    X = [[3], [4], [5], [6], [10], [15], [20], [25]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_Data = [[4.5], [12], [22]]

    pred = model.predict(new_Data)

    print("New data is:", new_Data)

    print("Prediction Results are :", pred)

if __name__ == "__main__":
    main()