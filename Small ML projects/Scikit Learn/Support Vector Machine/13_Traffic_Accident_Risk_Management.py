
# SVM - Traffic Accident Risk Classification

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Vehicle Speed (km/h), Traffic Density (vehicles)
    X = [
        [20, 10], [25, 15], [30, 20],
        [35, 25], [40, 30],
        [50, 60], [55, 65], [60, 70],
        [65, 75], [70, 80],
        [90, 20], [100, 15], [110, 10],
        [120, 25], [130, 30]
    ]

    # 0 = Low Risk, 1 = Medium Risk, 2 = High Risk
    y = [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2
    ]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="rbf")

    # Train model
    model.fit(X_scaled, y)

    # New traffic conditions
    new_conditions = [
        [30, 15],
        [60, 65],
        [110, 20]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_conditions)

    # Make predictions
    prediction = model.predict(new_scaled)

    risk_levels = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }

    print("Traffic Conditions:", new_conditions)
    print("Risk Predictions:", prediction)

    for i in range(len(prediction)):
        print("Condition", i + 1, ":", risk_levels[prediction[i]])


if __name__ == "__main__":
    main()
