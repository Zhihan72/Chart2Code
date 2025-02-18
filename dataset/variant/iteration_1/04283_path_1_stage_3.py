import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
solar = np.array([50, 70, 100, 150, 210, 300, 420, 550, 700, 850, 1000])
hydro = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
battery_storage = np.array([0, 5, 15, 30, 60, 120, 200, 310, 440, 580, 720])

total_consumption = solar + hydro + battery_storage
solar_share = (solar / total_consumption) * 100
hydro_share = (hydro / total_consumption) * 100
battery_storage_share = (battery_storage / total_consumption) * 100

fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Modifying style elements for the stackplot
axs[0].stackplot(years, solar, hydro, battery_storage, 
                 labels=['Solar', 'Hydro', 'Battery'], 
                 colors=['#8E44AD', '#3498DB', '#E74C3C'], alpha=0.85)
axs[0].set_title("Renewable Energy Adoption in TechVille (2015-2025)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Energy Consumption (GWh)", fontsize=12)
axs[0].legend(loc='upper right', title="Energy Source", frameon=False)
axs[0].grid(True, linestyle=':', alpha=0.6)
axs[0].set_xticks(years)
axs[0].set_xlim(2015, 2025)
axs[0].set_ylim(0, 2500)

# Modifying style elements for the line plots
axs[1].plot(years, solar_share, label='Solar', color='#8E44AD', marker='s', linestyle='--')
axs[1].plot(years, hydro_share, label='Hydro', color='#3498DB', marker='p', linestyle='-.')
axs[1].plot(years, battery_storage_share, label='Battery', color='#E74C3C', marker='*', linestyle=':')
axs[1].set_title("Energy Source Percentage Share in TechVille (2015-2025)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Percentage Share (%)", fontsize=12)
axs[1].legend(loc='lower right', title="Energy Source", frameon=True)
axs[1].grid(True, linestyle='-', alpha=0.8)
axs[1].set_xticks(years)
axs[1].set_xlim(2015, 2025)
axs[1].set_ylim(0, 100)

plt.tight_layout()
plt.show()