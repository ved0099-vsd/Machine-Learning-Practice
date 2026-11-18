
# SVM - Network Intrusion Detection

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Data Transferred (MB), Connection Duration (seconds)
    X = [
        [10, 20], [15, 25], [20, 30],
        [25, 35], [30, 40], [35, 45],
        [100, 5], [120, 8], [150, 10],
        [180, 12], [200, 15], [220, 18]
    ]

    # 0 = Normal, 1 = Suspicious
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

    # New network activity
    new_activity = [
        [18, 28],
        [130, 9],
        [200, 14]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_activity)

    # Predict network activity
    prediction = model.predict(new_scaled)

    print("Network Activity:", new_activity)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 0:
            print("Activity", i + 1, ": Normal")
        else:
            print("Activity", i + 1, ": Suspicious")

if __name__ == "__main__":
    main()
