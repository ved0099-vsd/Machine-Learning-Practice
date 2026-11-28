# SVM - Machine Fault Detection

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Temperature (°C), Vibration Level
    X = [
        [40, 2],
        [42, 3],
        [45, 2],
        [48, 4],
        [50, 3],
        [52, 5],
        [70, 12],
        [75, 15],
        [80, 18],
        [85, 20],
        [90, 22],
        [95, 25]
    ]

    # 0 = Normal, 1 = Fault
    y = [
        0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1
    ]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = SVC(kernel="rbf")
    model.fit(X_scaled, y)

    new_machines = [
        [43, 3],
        [78, 16],
        [92, 24]
    ]

    new_scaled = scaler.transform(new_machines)
    prediction = model.predict(new_scaled)

    print("Machine Details:", new_machines)
    print("Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 0:
            print("Machine", i + 1, ": Normal")
        else:
            print("Machine", i + 1, ": Fault Detected")

if __name__ == "__main__":
    main()