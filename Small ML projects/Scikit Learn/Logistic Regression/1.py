#Logistic Regression is a Machine Learning algorithm used mainly for classification — predicting a category.

from sklearn.linear_model import LogisticRegression

def main():
    X = [[1],[2],[3],[4],[5],[6]] # hours studied
    y = [0,0,0,0,1,1] # 0 = fail , 1= pass

# Create model
    model = LogisticRegression()

# Train the model
    model.fit(X,y)

# Predict for new study hours
    prediction = model.predict([[2], [5], [6]])

    print("Predicted results: ", prediction)

if __name__ == "__main__":
    main()