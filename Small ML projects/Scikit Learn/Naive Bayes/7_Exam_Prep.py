from sklearn.naive_bayes import GaussianNB

def main():
    # Study hours
    X = [[1], [2], [3], [4], [7], [8], [9], [10]]
    
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_data = [[2.5], [6], [9]]

    pred = model.predict(new_data)

    print("New data:",new_data)

    print("Predicted Results: ", pred)

if __name__ == "__main__":
    main()