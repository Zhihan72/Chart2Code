import matplotlib.pyplot as plt
import numpy as np

# Title and backstory
# Title: "Monthly Temperature Variation Across Cities"
# Backstory: We are conducting a study to analyze the temperature variation over the months in three different cities: Los Angeles, New York, and Chicago. This study aims to understand the seasonal change and how it affects each city's climate. 

# Data: Average monthly temperatures in Celsius for Los Angeles, New York, and Chicago
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
la_temps = np.array([14, 15, 17, 19, 22, 24, 27, 27, 26, 22, 18, 15])
ny_temps = np.array([0, 1, 7, 13, 19, 24, 27, 26, 22, 15, 10, 4])
chicago_temps = np.array([-3, 0, 6, 12, 18, 23, 26, 25, 20, 13, 6, -1])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line charts for each city
ax.plot(months, la_temps, marker='o', linestyle='-', color='orange', label='Los Angeles', linewidth=2)
ax.plot(months, ny_temps, marker='o', linestyle='-', color='blue', label='New York', linewidth=2)
ax.plot(months, chicago_temps, marker='o', linestyle='-', color='green', label='Chicago', linewidth=2)

# Customize the plot
ax.set_title("Monthly Temperature Variation Across Cities", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Average Temperature (°C)", fontsize=14)
ax.set_ylim(-5, 30)
ax.grid(True, linestyle='--', alpha=0.6)

# Adding data labels
for i, txt in enumerate(la_temps):
    ax.text(months[i], la_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color='orange')
for i, txt in enumerate(ny_temps):
    ax.text(months[i], ny_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color='blue')
for i, txt in enumerate(chicago_temps):
    ax.text(months[i], chicago_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color='green')

# Add a legend
ax.legend(title='Cities', title_fontsize='13', fontsize='10', loc='upper left')

# Ensure layout is adjusted
plt.tight_layout()

# Show the plot
plt.show()