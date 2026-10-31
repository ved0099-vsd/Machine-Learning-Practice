from sklearn.svm import SVC

def main():
    # Price
    X = [[500], [600], [700], [800], [1500], [1700], [1900], [2100]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = SVC(kernel="linear")

    model.fit(X,y)

    new_prices = [[650], [1200], [2000]]

    pred = model.predict(new_prices)

    print("New Data is ", new_prices)
    print("Predicted Results :", pred)

if __name__ == "__main__":
    main()