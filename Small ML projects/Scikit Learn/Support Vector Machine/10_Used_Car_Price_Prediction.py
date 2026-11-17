
# SVM - Used Car Price Category Prediction

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Car Age (Years), Kilometres Driven (Thousands)
    X = [
        [1, 10], [2, 20], [3, 30],
        [4, 40], [5, 50], [3, 60],
        [6, 70], [7, 80], [8, 90],
        [9, 100], [10, 120], [12, 150],
        [2, 15], [5, 55], [11, 130]
    ]

    # 0 = Budget, 1 = Mid-Range, 2 = Premium
    y = [
        2, 2, 2, 1, 1,
        1, 1, 0, 0, 0,
        0, 0, 2, 1, 0
    ]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="rbf")

    # Train model
    model.fit(X_scaled, y)

    # New car details
    new_cars = [
        [10, 110],
        [5, 45],
        [2, 12]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_cars)

    # Predict car categories
    prediction = model.predict(new_scaled)

    categories = {
        0: "Budget",
        1: "Mid-Range",
        2: "Premium"
    }

    print("Car Details:", new_cars)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        print("Car", i + 1, ":", categories[prediction[i]])

if __name__ == "__main__":
    main()
