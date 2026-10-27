from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Soil Moisture Percentage, Sunlight Hours]
    X = [
        [10, 1], [15, 2], [20, 2], [25, 3],
        [40, 5], [50, 6], [60, 7], [70, 8]
    ]

    # 0 = Unhealthy, 1 = Healthy
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_plants = [[50, 2], [45, 50], [1, 17]]

    pred = model.predict(new_plants)

    print("new Data : ", new_plants)

    print("predicted data :", pred)


if __name__ == "__main__":
    main()