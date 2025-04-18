import matplotlib.pyplot as plt
import numpy as np

# Define the years from 1960 to 2020
years = np.arange(1960, 2021)

# Define the budget allocations in billions
satellites = np.array([0.5, 0.8, 1.1, 1.5, 2.0, 2.5, 3.0, 4.0, 4.5, 5.0, 6.0, 7.0, 8.5, 10.0, 11.5, 13.0, 15.0, 17.0, 19.0, 21.0, 23.5, 26.0, 28.5, 31.0, 34.0, 37.0, 40.5, 44.0, 48.0, 52.5, 57.0, 62.0, 67.0, 72.0, 77.0, 83.0, 89.0, 95.0, 102.0, 109.0, 117.0, 125.0, 134.0, 144.0, 155.0, 167.0, 180.0, 194.0, 209.0, 225.0, 243.0, 262.0, 282.0, 303.0, 325.0, 348.0, 372.0, 398.0, 425.0, 453.0, 482.0])
missions = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.7, 2.0, 2.3, 2.7, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.5, 22.0, 23.5, 25.0, 26.5, 28.0, 29.5, 31.0, 32.5, 34.0, 35.5, 37.0, 38.5, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0])

# Create the stacked area plot
plt.figure(figsize=(14, 8))

plt.stackplot(years, satellites, missions,
              labels=['Satellites', 'Manned Missions'],
              colors=['#FF9999', '#99FF99'], alpha=0.7)

# Title and labels
plt.title("Global Space Exploration Budgets (1960-2020)\nInvestments in Satellites and Manned Missions", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Budget Allocation (Billions USD)", fontsize=12)

# Legend
plt.legend(loc='upper left', fontsize=10, title="Space Exploration Sectors")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()