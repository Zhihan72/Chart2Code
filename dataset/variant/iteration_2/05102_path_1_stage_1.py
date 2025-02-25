import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Manually altered data for energy production (in TWh)
hydropower = np.array([115, 127, 133, 130, 142, 150, 145, 155, 158, 160, 162])
solar = np.array([7, 9, 11, 20, 28, 34, 43, 62, 78, 95, 125])
wind = np.array([12, 17, 24, 28, 40, 49, 57, 77, 89, 105, 136])
fossil_fuels = np.array([305, 285, 275, 265, 255, 245, 230, 215, 205, 185, 168])
nuclear = 700 - (hydropower + solar + wind + fossil_fuels)

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stack plot for energy production sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax1.stackplot(years, hydropower, solar, wind, fossil_fuels, labels=['Hydropower', 'Solar', 'Wind', 'Fossil Fuels'], colors=colors, alpha=0.85)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (TWh)', fontsize=12, color='k')
ax1.set_title('Evolution of Energy Production Mix in Renewable Town\n(2010-2020)', fontsize=16, weight='bold')

# Adding grid for better readability
ax1.grid(alpha=0.3)

# Add a legend for the stack plot
ax1.legend(loc='upper left', title='Energy Sources', fontsize=10)

# Line plot for nuclear energy production
ax2 = ax1.twinx()
ax2.plot(years, nuclear, color='purple', marker='o', linestyle='--', linewidth=2.5, label='Nuclear Energy')
ax2.set_ylabel('Nuclear Energy Production (TWh)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Add a legend for the line plot
ax2.legend(loc='upper right', fontsize=10)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()