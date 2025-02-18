import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
months = range(1, 13)

temperature_data = [
    [55.3, 65.2, 30.5, 45.2, 32.1, 75.1, 80.0, 78.9, 70.3, 59.2, 45.1, 35.4],
    [31.2, 33.0, 46.5, 56.0, 66.1, 76.0, 80.3, 79.5, 71.1, 60.0, 46.0, 36.0],
    [30.8, 32.5, 45.7, 55.8, 65.8, 75.7, 80.5, 79.0, 70.8, 59.8, 45.9, 35.8],
    [31.0, 33.2, 46.3, 56.3, 66.5, 76.5, 81.0, 79.7, 71.5, 60.5, 46.5, 36.3],
    [30.9, 32.8, 45.9, 55.6, 65.9, 75.6, 80.8, 78.8, 70.6, 59.5, 45.6, 35.7],
    [31.5, 46.8, 56.8, 33.5, 66.8, 76.8, 81.5, 80.0, 71.8, 60.8, 46.8, 36.8],
    [31.8, 33.9, 47.2, 57.2, 67.2, 77.2, 82.0, 80.5, 72.2, 61.2, 47.2, 37.2],
    [32.0, 34.0, 47.5, 57.5, 67.5, 77.5, 82.5, 81.0, 73.0, 62.0, 47.5, 37.5],
    [32.3, 34.3, 58.0, 48.0, 68.0, 78.0, 83.0, 81.5, 73.5, 62.5, 48.0, 38.0],
    [32.5, 34.5, 48.5, 58.5, 68.5, 78.5, 83.5, 82.0, 74.0, 63.0, 48.5, 38.5]
]

temperature_data = np.array(temperature_data)

# Define a new set of colors that will be applied to each line plot
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
          '#ffb3e6', '#ff6666', '#c44dff', '#80ff80', '#80b3ff']

plt.figure(figsize=(14, 8))

# Apply the new color set for each year's line plot
for i, color in enumerate(colors):
    plt.plot(months, temperature_data[i], marker='o', linestyle='-', color=color)

plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Temperature (°F)", fontsize=12)
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.tight_layout()
plt.show()