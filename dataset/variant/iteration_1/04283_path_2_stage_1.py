import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.arange(2015, 2026)

# Renewable energy consumption data in GWh
solar = np.array([50, 70, 100, 150, 210, 300, 420, 550, 700, 850, 1000])
wind = np.array([30, 50, 80, 120, 160, 200, 250, 310, 350, 400, 450])
hydro = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
battery_storage = np.array([0, 5, 15, 30, 60, 120, 200, 310, 440, 580, 720])

# Calculate total consumption per year and percentage shares
total_consumption = solar + wind + hydro + battery_storage
solar_share = (solar / total_consumption) * 100
wind_share = (wind / total_consumption) * 100
hydro_share = (hydro / total_consumption) * 100
battery_storage_share = (battery_storage / total_consumption) * 100

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Stacked area plot for renewable energy consumption
axs[0].stackplot(years, solar, wind, hydro, battery_storage, 
                 labels=['Solar', 'Wind', 'Hydro', 'Battery'], 
                 colors=['#32CD32', '#8B4513', '#FFD700', '#1E90FF'], alpha=0.85)
axs[0].set_title("Renewable Energy Adoption in TechVille (2015-2025)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Energy Consumption (GWh)", fontsize=12)
axs[0].legend(loc='upper left', title="Energy Source")
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].set_xticks(years)
axs[0].set_xlim(2015, 2025)
axs[0].set_ylim(0, 2500)

# Line plot for percentage share of each energy source
axs[1].plot(years, solar_share, label='Solar', color='#32CD32', marker='o')
axs[1].plot(years, wind_share, label='Wind', color='#8B4513', marker='s')
axs[1].plot(years, hydro_share, label='Hydro', color='#FFD700', marker='^')
axs[1].plot(years, battery_storage_share, label='Battery', color='#1E90FF', marker='D')
axs[1].set_title("Energy Source Percentage Share in TechVille (2015-2025)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Percentage Share (%)", fontsize=12)
axs[1].legend(loc='upper left', title="Energy Source")
axs[1].grid(True, linestyle='--', alpha=0.7)
axs[1].set_xticks(years)
axs[1].set_xlim(2015, 2025)
axs[1].set_ylim(0, 100)

# Automatically adjust layout to prevent overlapping of elements
plt.tight_layout()

# Show the chart
plt.show()