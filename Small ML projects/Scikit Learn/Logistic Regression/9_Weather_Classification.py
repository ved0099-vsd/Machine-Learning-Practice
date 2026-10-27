from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Humidity Percentage
    X = [[20], [25], [30], [35], [40],
         [50], [60], [70], [80], [90]]

    # 0 = No Rain, 1 = Rain
    y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_weather = [[30], [60], [85]]

    prediction = model.predict(new_weather)

    print("Predicted results are :",prediction)

if __name__ == "__main__":
    main()