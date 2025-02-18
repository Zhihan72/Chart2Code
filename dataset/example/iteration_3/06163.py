import matplotlib.pyplot as plt
import numpy as np

# Fictional backstory:
# Over the past 5 years, the town of Aquaville has seen a significant increase in the consumption of different types of beverages. These beverages include water, coffee, tea, and soda. This data is collected from surveys conducted each month, showing the average monthly consumption of these beverages from the years 2018 to 2022. The town administration wants this data visualized to understand trends and make better decisions regarding resource allocation. This plot will help identify consumption trends and the relative popularity of each beverage over time.

# Define years from 2018 to 2022
years = np.arange(2018, 2023)

# Monthly consumption of different beverages in liters (fictional data)
water = np.array([50, 55, 60, 65, 70])
coffee = np.array([20, 22, 24, 28, 30])
tea = np.array([15, 16, 18, 20, 22])
soda = np.array([10, 12, 14, 16, 18])

# Stack the data
data = np.vstack([water, coffee, tea, soda])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the stacked area plot
ax.stackplot(years, data, labels=['Water', 'Coffee', 'Tea', 'Soda'],
             colors=['#add8e6', '#8a735b', '#98fb98', '#ffb6c1'], alpha=0.8)

# Add title and labels
ax.set_title('Beverage Consumption Trends in Aquaville\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Consumption (liters)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Beverages')

# Customize the grid
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Customize x-axis labels
plt.xticks(rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()