
# SVM - Vehicle Theft Detection

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Vehicle Speed (km/h), Distance Travelled (km)
    X = [
        [20, 2],
        [30, 3],
        [40, 4],
        [50, 5],
        [60, 6],
        [80, 30],
        [90, 40],
        [100, 50],
        [110, 60],
        [120, 70],
        [130, 80],
        [140, 90]
    ]

    # 0 = Normal Activity, 1 = Suspicious Activity
    y = [
        0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1
    ]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="rbf")

    # Train model
    model.fit(X_scaled, y)

    # New vehicle activity
    new_activity = [
        [35, 3],
        [85, 35],
        [125, 75]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_activity)

    # Predict activity
    prediction = model.predict(new_scaled)

    print("Vehicle Activity:", new_activity)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 0:
            print("Vehicle", i + 1, ": Normal Activity")
        else:
            print("Vehicle", i + 1, ": Suspicious Activity")

if __name__ == "__main__":
    main()
