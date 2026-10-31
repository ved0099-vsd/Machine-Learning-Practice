from sklearn.svm import SVC

def main():
    X = [[2], [5], [8], [10], [50], [60], [70], [80]]

    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = SVC(kernel="linear")

    model.fit(X,y)

    new_data = [[6], [35], [75]]

    pred = model.predict(new_data)

    print("New data is :", new_data)

    print("Predicted Results:", pred)

if __name__ == "__main__":
    main()