# Split → Create model → Train → Predict on X_test → Compare with y_test

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    X = [[5], [10], [15], [20], [25],
     [30], [35], [40], [45], [50]]

    y = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42, test_size=0.2)

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    prediction = model.predict(X_test)

    print("Actual Prediction",y_test)
    print("Prediction results :",prediction)

if __name__ == "__main__":
    main()