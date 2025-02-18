import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

hydropower = np.array([120, 125, 130, 135, 140, 145, 148, 150, 152, 155, 160])
solar = np.array([5, 8, 12, 18, 25, 35, 45, 60, 80, 100, 130])
wind = np.array([10, 15, 22, 30, 38, 47, 60, 75, 90, 110, 135])
fossil_fuels = np.array([300, 290, 280, 270, 260, 250, 235, 220, 210, 190, 165])
nuclear = 700 - (hydropower + solar + wind + fossil_fuels)

fig, ax1 = plt.subplots(figsize=(14, 8))

# New color scheme: purple, gold, teal, brown
colors = ['#9467bd', '#bcbd22', '#17becf', '#8c564b']  
ax1.stackplot(years, hydropower, solar, wind, fossil_fuels, labels=['Hydropower', 'Solar', 'Wind', 'Fossil Fuels'], colors=colors, alpha=0.85)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (TWh)', fontsize=12, color='k')
ax1.set_title('Evolution of Energy Production Mix in Renewable Town\n(2010-2020)', fontsize=16, weight='bold')

ax1.grid(alpha=0.3)
ax1.legend(loc='upper left', title='Energy Sources', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(years, nuclear, color='purple', marker='o', linestyle='--', linewidth=2.5, label='Nuclear Energy')
ax2.set_ylabel('Nuclear Energy Production (TWh)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()