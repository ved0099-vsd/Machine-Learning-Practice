
# SVM - Customer Churn Prediction

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

def main():

    # Features: Subscription Duration (months), Monthly Charges
    X = [
        [1, 900], [2, 850], [3, 800], [4, 750],
        [12, 500], [18, 450], [24, 400], [36, 350],
        [6, 700], [30, 380]
    ]

    # 0 = Stay, 1 = Leave
    y = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create SVM model
    model = SVC(kernel="linear")

    # Train model
    model.fit(X_scaled, y)

    # New customer details
    new_customers = [
        [2, 880],
        [15, 480],
        [32, 360]
    ]

    # Scale new customer data
    new_scaled = scaler.transform(new_customers)

    # Make predictions
    prediction = model.predict(new_scaled)

    print("Customer Details:", new_customers)
    print("Churn Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 1:
            print("Customer", i + 1, ": Likely to Leave")
        else:
            print("Customer", i + 1, ": Likely to Stay")


if __name__ == "__main__":
    main()
