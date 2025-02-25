import matplotlib.pyplot as plt
import numpy as np

# Define the months and temperature data for each city
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
city1_temp = np.array([5, 7, 10, 15, 20, 25, 30, 29, 23, 17, 10, 6])
city3_temp = np.array([0, 2, 8, 12, 17, 22, 27, 26, 21, 15, 8, 3])

# Setup subplot figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting line charts for each city's temperature
ax.plot(months, city1_temp, marker='o', linestyle='-', color='b')
ax.plot(months, city3_temp, marker='d', linestyle='-.', color='g')

# Adding titles and labels
ax.set_title("Monthly Temperature Variations for Different Cities in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=12)
ax.set_ylabel("Temperature (°C)", fontsize=12)

# Adding values on each data point
for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.5, f"{city1_temp[i]}°C", ha='center', va='bottom', fontsize=9)
    ax.text(months[i], city3_temp[i] + 0.5, f"{city3_temp[i]}°C", ha='center', va='bottom', fontsize=9)

# Adjust layout to fit everything properly
plt.tight_layout()

# Display the plot
plt.show()