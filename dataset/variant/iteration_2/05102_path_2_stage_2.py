import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

hydropower = np.array([120, 125, 130, 135, 140, 145, 148, 150, 152, 155, 160])
solar = np.array([5, 8, 12, 18, 25, 35, 45, 60, 80, 100, 130])
wind = np.array([10, 15, 22, 30, 38, 47, 60, 75, 90, 110, 135])
fossil_fuels = np.array([300, 290, 280, 270, 260, 250, 235, 220, 210, 190, 165])
nuclear = 700 - (hydropower + solar + wind + fossil_fuels)

fig, ax1 = plt.subplots(figsize=(14, 8))

# New color scheme
colors = ['#ff7f0e', '#1f77b4', '#d62728', '#2ca02c']  
ax1.stackplot(years, hydropower, solar, wind, fossil_fuels, labels=['Hydropower', 'Solar', 'Wind', 'Fossil Fuels'], colors=colors)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (TWh)', fontsize=12)
ax1.set_title('Energy Production Mix in Renewable Town (2010-2020)', fontsize=16)

# Adjust grid and border
ax1.grid(alpha=0.6, linestyle='--', color='grey')

ax1.legend(loc='lower left', title='Energy Sources', fontsize=11, frameon=True, shadow=True)

ax2 = ax1.twinx()
ax2.plot(years, nuclear, color='black', marker='s', linestyle=':', linewidth=3, label='Nuclear Energy')
ax2.set_ylabel('Nuclear Energy Production (TWh)', fontsize=12, color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.legend(loc='lower right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()