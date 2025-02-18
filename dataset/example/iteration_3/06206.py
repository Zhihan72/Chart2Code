import matplotlib.pyplot as plt
import numpy as np

# The backstory: We are plotting the fictional "City X Urban Transportation Trend" showing the shifting popularity of various transportation modes (Biking, Walking, Public Transport, Personal Cars) over a decade from 2010 to 2020.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Synthetic data for the different transportation modes over the years (in percentage)
biking = np.array([5, 7, 8, 12, 14, 15, 16, 18, 20, 22, 25])
walking = np.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15])
public_transport = np.array([40, 38, 37, 36, 35, 34, 33, 32, 31, 30, 28])
personal_cars = np.array([30, 31, 32, 30, 30, 31, 32, 32, 32, 32, 32])

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting each line with different styles and markers
ax.plot(years, biking, label='Biking', color='green', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, walking, label='Walking', color='orange', marker='s', linestyle='--', linewidth=2, markersize=6)
ax.plot(years, public_transport, label='Public Transport', color='blue', marker='d', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, personal_cars, label='Personal Cars', color='red', marker='^', linestyle=':', linewidth=2, markersize=6)

# Customizing the title and labels
plt.title("City X Urban Transportation Trend (2010-2020)", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Usage Percentage (%)", fontsize=14)

# Adding a legend to explain the lines
plt.legend(title='Transportation Modes', loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title_fontsize='13')

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-ticks for better visibility
ax.set_xticks(years)
plt.xticks(rotation=45)

# Automatically adjust layout for a clean visual representation
plt.tight_layout()

# Display the plot
plt.show()