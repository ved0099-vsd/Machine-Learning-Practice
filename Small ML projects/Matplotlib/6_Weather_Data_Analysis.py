
import numpy as np
import matplotlib.pyplot as plt

def main():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    temperature = np.array([30, 32, 31, 29, 33, 35, 34])
    humidity = np.array([65, 60, 70, 75, 55, 50, 58])

    # 1. Weekly Temperature Graph
    plt.figure(figsize=(8, 5))
    plt.plot(days, temperature, marker="o")
    plt.title("Weekly Temperature Analysis")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.savefig("weekly_temperature.png")
    plt.show()

    # 2. Daily Humidity Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(days, humidity)
    plt.title("Daily Humidity")
    plt.xlabel("Days")
    plt.ylabel("Humidity (%)")
    plt.grid(axis="y")
    plt.savefig("daily_humidity.png")
    plt.show()

    # 3. Temperature Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(temperature, bins=5, edgecolor="black")
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Number of Days")
    plt.savefig("temperature_distribution.png")
    plt.show()

    # 4. Weather Statistics
    print("Average Temperature:", np.mean(temperature))
    print("Highest Temperature:", np.max(temperature))
    print("Lowest Temperature:", np.min(temperature))
    print("Average Humidity:", np.mean(humidity))
    print("Days Above 32°C:", np.sum(temperature > 32))

if __name__ == "__main__":
    main()