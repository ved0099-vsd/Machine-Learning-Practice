from sklearn.naive_bayes import GaussianNB

def main():
    # Humidity Percentage
    X = [[20], [25], [30], [35], [60], [70], [80], [90]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_Data = [[28], [55], [85]]

    pred = model.predict(new_Data)

    print("New Data :",new_Data)

    print("Predicted Results:", pred)

if __name__ == "__main__":
    main()