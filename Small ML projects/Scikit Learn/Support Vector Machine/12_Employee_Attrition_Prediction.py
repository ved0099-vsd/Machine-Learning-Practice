
# SVM - Employee Attrition Prediction

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Experience (Years), Job Satisfaction (1-10)
    X = [
        [1, 2], [2, 3], [3, 2],
        [4, 3], [5, 4], [6, 5],
        [2, 8], [3, 9], [5, 8],
        [7, 9], [8, 8], [10, 9]
    ]

    # 0 = Stay, 1 = Leave
    y = [
        1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0
    ]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="rbf")

    # Train model
    model.fit(X_scaled, y)

    # New employee details
    new_employees = [
        [2, 2],
        [5, 7],
        [9, 9]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_employees)

    # Predict employee attrition
    prediction = model.predict(new_scaled)

    print("Employee Details:", new_employees)
    print("Attrition Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 1:
            print("Employee", i + 1, ": Likely to Leave")
        else:
            print("Employee", i + 1, ": Likely to Stay")

if __name__ == "__main__":
    main()
