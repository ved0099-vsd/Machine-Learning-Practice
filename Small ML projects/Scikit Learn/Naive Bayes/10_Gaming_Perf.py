from sklearn.naive_bayes import GaussianNB

def main():
    # FPS
    X = [[10], [15], [20], [25], [50], [60], [70], [80]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = GaussianNB()

    model.fit(X,y)

    new_data = [[18], [40], [75]]

    pred = model.predict(new_data)

    print("New Data :",new_data)

    print("Prediction Results", pred)

if __name__ == "__main__":
    main()