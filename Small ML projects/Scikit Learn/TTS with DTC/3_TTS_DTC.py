from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    X = [[10], [20], [30], [40], [50],
     [60], [70], [80], [90], [100]]

    y = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    prediction = model.predict(X_test)

    print("Actual Prediction :",y_test)
    print("Prediction", prediction)
    

if __name__ == "__main__":
    main()