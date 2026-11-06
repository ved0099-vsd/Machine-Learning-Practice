from sklearn.svm import SVC

def main():

    # Features: Car Age (years), Kilometres Driven (thousands)
    X = [
        [1, 10],
        [2, 20],
        [3, 30],
        [4, 40],
        [8, 100],
        [9, 120],
        [10, 140],
        [12, 160]
    ]

    # 0 = Poor Condition, 1 = Good Condition
    y = [1, 1, 1, 1, 0, 0, 0, 0]

    # Create SVM model
    model = SVC(kernel="linear")

    # Train model
    model.fit(X, y)

    # Predict new cars
    new_cars = [
        [2, 15],
        [5, 60],
        [10, 130]
    ]

    prediction = model.predict(new_cars)

    print("Car Details:", new_cars)
    print("Condition Predictions:", prediction)

if __name__ == "__main__":
    main()