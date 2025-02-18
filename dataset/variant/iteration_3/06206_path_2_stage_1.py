import matplotlib.pyplot as plt
import numpy as np

# Time period covering 2010 to 2020
years = np.arange(2010, 2021)

# Transportation data in percentages
biking = np.array([5, 7, 8, 12, 14, 15, 16, 18, 20, 22, 25])
walking = np.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15])
public_transport = np.array([40, 38, 37, 36, 35, 34, 33, 32, 31, 30, 28])
personal_cars = np.array([30, 31, 32, 30, 30, 31, 32, 32, 32, 32, 32])

fig, ax = plt.subplots(figsize=(10, 6))

# Plot each transportation mode with unique styles
ax.plot(years, biking, label='Bicycles', color='green', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, walking, label='Pedestrians', color='orange', marker='s', linestyle='--', linewidth=2, markersize=6)
ax.plot(years, public_transport, label='Buses & Trains', color='blue', marker='d', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, personal_cars, label='Automobiles', color='red', marker='^', linestyle=':', linewidth=2, markersize=6)

# Modify title and label texts
plt.title("Urban Shift in Transportation (2010-2020)", fontsize=16, weight='bold', pad=20)
plt.xlabel("Timeline", fontsize=14)
plt.ylabel("Percentage of Usage", fontsize=14)

# Legend to interpret plot lines
plt.legend(title='Modes of Travel', loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title_fontsize='13')

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-ticks for better visibility
ax.set_xticks(years)
plt.xticks(rotation=45)

# Automatically adjust layout for a clean visual representation
plt.tight_layout()

# Display the plot
plt.show()