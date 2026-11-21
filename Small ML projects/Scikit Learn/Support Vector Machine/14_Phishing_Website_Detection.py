
# SVM - Phishing Website Detection

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: URL Length, Suspicious Character Count
    X = [
        [15, 0],
        [20, 1],
        [25, 0],
        [30, 1],
        [35, 0],
        [50, 4],
        [60, 5],
        [70, 6],
        [80, 7],
        [90, 8],
        [100, 9],
        [110, 10]
    ]

    # 0 = Legitimate, 1 = Phishing
    y = [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1
    ]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="rbf")

    # Train model
    model.fit(X_scaled, y)

    # New website details
    new_websites = [
        [20, 0],
        [65, 5],
        [100, 9]
    ]

    # Scale new data
    new_scaled = scaler.transform(new_websites)

    # Predict website categories
    prediction = model.predict(new_scaled)

    print("Website Features:", new_websites)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 0:
            print("Website", i + 1, ": Legitimate")
        else:
            print("Website", i + 1, ": Phishing")

if __name__ == "__main__":
    main()