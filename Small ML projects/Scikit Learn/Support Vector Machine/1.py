# SVM is a supervised machine learning algorithm used for classification and regression. 
# Its main idea is to find the best boundary (called a hyperplane) that separates different classes.

from sklearn.svm import SVC

def main():
        # Feature: Fruit weight in grams
    X = [[100], [120], [130], [140],
         [180], [200], [220], [250]]

    # 0 = Apple, 1 = Orange
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = SVC(kernel="linear")
    model.fit(X,y)

    new_fruits = [[110], [190], [240]]

    prediction = model.predict(new_fruits)

    print("Fruit Weights,",new_fruits)
    print("fruit Predictions,", prediction)

if __name__ == "__main__":
    main()