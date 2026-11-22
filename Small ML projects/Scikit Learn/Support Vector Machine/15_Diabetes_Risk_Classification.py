
# SVM - Diabetes Risk Classification

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Glucose Level, BMI
    X = [
        [85, 20],
        [90, 22],
        [95, 23],
        [100, 24],
        [105, 25],
        [130, 30],
        [140, 32],
        [150, 35],
        [160, 36],
        [170, 38],
        [180, 40],
        [190, 42]
    ]

    # 0 = Lower Risk, 1 = Higher Risk
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

    # New records
    new_records = [
        [92, 22],
        [125, 29],
        [175, 39]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_records)

    # Make predictions
    prediction = model.predict(new_scaled)

    print("Patient Data:", new_records)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 0:
            print("Record", i + 1, ": Lower Risk")
        else:
            print("Record", i + 1, ": Higher Risk")

if __name__ == "__main__":
    main()
