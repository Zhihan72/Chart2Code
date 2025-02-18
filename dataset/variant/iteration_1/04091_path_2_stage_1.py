import matplotlib.pyplot as plt
import numpy as np

# Data: Energy generation by different sources from 2010 to 2020
years = np.arange(2010, 2021)
solar = np.array([5, 10, 18, 30, 45, 65, 90, 120, 155, 200, 250])
wind = np.array([10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 340])
hydro = np.array([60, 63, 65, 68, 70, 72, 74, 76, 78, 80, 82])
fossil = np.array([300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200])
nuclear = np.array([50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70])  # New data group added

# Cumulatively stack data
renewable = solar + wind + hydro
total = renewable + fossil + nuclear

# Create the figure and axes for subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16, 12))

# Plot area chart for energy sources over the years
ax1.stackplot(
    years, solar, wind, hydro, fossil, nuclear, 
    labels=['Solar', 'Wind', 'Hydro', 'Fossil', 'Nuclear'],
    colors=['#FFD700', '#7FFFD4', '#1E90FF', '#B22222', '#FF8C00'], alpha=0.7
)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Generation (GWh)', fontsize=14)
ax1.set_title('Decade of Energy Transition:\nGeneration by Source', fontsize=18, fontweight='bold')
ax1.legend(loc='upper left', title='Energy Source')
ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax1.annotate('Rise of Renewables', xy=(2015, 150), xytext=(2012, 300),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Plot area chart for cumulative energy generation (total) and renewable contribution
ax2.fill_between(years, 0, total, label='Total Energy Generation', color='lightsteelblue', alpha=0.7)
ax2.fill_between(years, 0, renewable + nuclear, label='Renewable & Nuclear Energy', color='lightgreen', alpha=0.8)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Total Energy Generation (GWh)', fontsize=14)
ax2.set_title('Cumulative Energy Generation by Year', fontsize=18, fontweight='bold')
ax2.legend(loc='upper left', title='Energy Type')
ax2.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax2.annotate(
    'Renewables + Nuclear Share in 2020',
    xy=(2020, renewable[-1] + nuclear[-1]), xytext=(2017, renewable[-1] + nuclear[-1] + 100),
    arrowprops=dict(arrowstyle='->', connectionstyle="arc3", facecolor='black', shrinkA=5, shrinkB=5),
    fontsize=12
)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()