# Split → Create model → Train → Predict → Compare

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():

    X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]] # study hours
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] # result


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)
# The model learns patterns from the training data only.

    prediction = model.predict(X_test)
# The model predicts the labels for the two test inputs.

    print("Actual Results :", y_test)
    print("Predicted Results :",prediction)

if __name__ =="__main__":
    main()