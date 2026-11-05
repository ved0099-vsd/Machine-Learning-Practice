from sklearn.svm import SVC

def main():

    # Features: RAM (GB), Processor Speed (GHz)
    X = [
        [4, 2.0],
        [4, 2.5],
        [8, 2.2],
        [8, 2.8],
        [16, 3.5],
        [16, 4.0],
        [32, 3.8],
        [32, 4.5]
    ]

    # 0 = Basic, 1 = High Performance
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    # Create model
    model = SVC(kernel="linear")

    # Train model
    model.fit(X, y)

    # Predict new laptops
    new_laptops = [[4, 2.3], [8, 2.6], [32, 4.2]]

    prediction = model.predict(new_laptops)

    print("Laptop Specifications:", new_laptops)
    print("Performance:", prediction)

if __name__ == "__main__":
    main()