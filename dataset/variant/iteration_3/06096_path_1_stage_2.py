import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding values for different metrics
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_share = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
revenue = np.array([1, 2, 3.5, 5, 7.5, 10, 13.5, 17, 22])
rnd_investment = np.array([0.2, 0.5, 0.8, 1.2, 1.8, 2.5, 4, 5.5, 7])
employee_growth = np.array([50, 60, 80, 110, 150, 200, 270, 350, 450])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot area charts for different metrics
ax.fill_between(years, market_share, color='mediumslateblue', alpha=0.6)
ax.fill_between(years, revenue, color='mediumseagreen', alpha=0.6)
ax.fill_between(years, rnd_investment, color='salmon', alpha=0.6)
ax.fill_between(years, employee_growth, color='gold', alpha=0.6)

# Add grids
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()