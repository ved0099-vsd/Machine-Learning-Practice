
import numpy as np

def main():
    Marks = np.array([
        [68, 85, 92],
        [74, 59, 81],
        [91, 77, 64],
        [55, 88, 79]
    ])

    print(Marks)

    

    # Q1. Display the mark 81
    print("Q1. Mark 81:")
    print(Marks[1, 2])

    # Q2. Display the first two columns of all students
    print("\nQ2. First two columns:")
    print(Marks[:, :2])

    # Q3. Calculate total marks of each student
    print("\nQ3. Total marks of each student:")
    print(np.sum(Marks, axis=1))

    # Q4. Calculate average marks in each subject
    print("\nQ4. Average marks in each subject:")
    print(np.mean(Marks, axis=0))

    # Q5. Display all marks greater than 80
    print("\nQ5. Marks greater than 80:")
    print(Marks[Marks > 80])

    # Q6. Count marks below 70
    print("\nQ6. Count of marks below 70:")
    print(np.sum(Marks < 70))

    # Q7. Sort the third student's marks in descending order
    print("\nQ7. Third student's marks in descending order:")
    print(np.sort(Marks[2])[::-1])

    # Q8. Find minimum and maximum marks
    print("\nQ8. Minimum mark:")
    print(np.min(Marks))

    print("Maximum mark:")
    print(np.max(Marks))

    # Q9. Display shape, size, and dimensions
    print("\nQ9. Shape:")
    print(Marks.shape)

    print("Size:")
    print(Marks.size)

    print("Number of dimensions:")
    print(Marks.ndim)

    # Q10. Reshape into 3 rows and 4 columns
    print("\nQ10. Reshaped array (3 rows, 4 columns):")
    print(Marks.reshape(3, 4))


if __name__ == "__main__":
    main()
