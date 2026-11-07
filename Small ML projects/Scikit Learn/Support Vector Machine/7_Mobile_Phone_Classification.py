from sklearn.svm import SVC

def main():
        # Features: RAM (GB), Battery Capacity (mAh)
    X = [
        [2, 3000],
        [3, 3200],
        [4, 3500],
        [4, 4000],
        [8, 4500],
        [8, 5000],
        [12, 5000],
        [16, 5500]
    ]

    # 0 = Basic, 1 = Premium
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = SVC(kernel="linear")

    model.fit(X,y)

    new = [
        [3, 3100],
        [6, 4200],
        [12, 5200]
    ]

    pred = model.predict(new)

    print("NEW pHONES Are :", new)
    print("Predicted Results are :", pred)
    

if __name__ == "__main__":
    main()