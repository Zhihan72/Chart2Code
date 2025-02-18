import matplotlib.pyplot as plt
import numpy as np

# Define the months and temperature data for each city
months = np.array(["Mar", "May", "Feb", "Aug", "Jun", "Apr", "Sep", "Jul", "Oct", "Nov", "Dec", "Jan"])
city1_temp = np.array([10, 20, 7, 29, 25, 15, 23, 30, 17, 10, 6, 5])
city3_temp = np.array([8, 17, 2, 26, 22, 12, 21, 27, 15, 8, 3, 0])

# Setup subplot figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting line charts for each city's temperature
ax.plot(months, city1_temp, marker='o', linestyle='-', color='b')
ax.plot(months, city3_temp, marker='d', linestyle='-.', color='g')

# Adding titles and labels
ax.set_title("City Temperature Changes Throughout 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Time of Year", fontsize=12)
ax.set_ylabel("Degrees Celsius", fontsize=12)

# Adding values on each data point
for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.5, f"{city1_temp[i]}°C", ha='center', va='bottom', fontsize=9)
    ax.text(months[i], city3_temp[i] + 0.5, f"{city3_temp[i]}°C", ha='center', va='bottom', fontsize=9)

# Adjust layout to fit everything properly
plt.tight_layout()

# Display the plot
plt.show()