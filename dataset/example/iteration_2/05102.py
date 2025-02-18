import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Analysis of Energy Production Mix Over a Decade (2010-2020)
# This chart illustrates the change in the energy production mix (in terawatt-hours, TWh) from various sources in Renewable Town, reflecting a gradual shift towards sustainable energy sources over a decade.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data representing energy production from various sources (in TWh)
hydropower = np.array([120, 125, 130, 135, 140, 145, 148, 150, 152, 155, 160])
solar = np.array([5, 8, 12, 18, 25, 35, 45, 60, 80, 100, 130])
wind = np.array([10, 15, 22, 30, 38, 47, 60, 75, 90, 110, 135])
fossil_fuels = np.array([300, 290, 280, 270, 260, 250, 235, 220, 210, 190, 165])
nuclear = 700 - (hydropower + solar + wind + fossil_fuels)  # Ensure total adds up to 700 TWh

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stack plot for energy production sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # blue, orange, green, red
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