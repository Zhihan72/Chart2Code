import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2000, 2021)

solar = np.array([
    5, 10, 15, 20, 30, 45, 60, 85, 110, 140,
    175, 215, 250, 295, 350, 410, 475, 550, 640, 740, 850
])
wind = np.array([
    10, 15, 20, 30, 45, 60, 75, 90, 110, 130,
    155, 185, 220, 265, 320, 380, 450, 530, 620, 720, 830
])

energy_data = np.vstack([solar, wind])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#00BFFF']

ax.stackplot(years, energy_data, colors=colors, alpha=0.85)

ax.set_title("Energy Trends in Renewable Sectors\n(2000-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Timeline (Years)', fontsize=14)
ax.set_ylabel('Usage (GW)', fontsize=14)

ax.annotate('Solar Investment', xy=(2015, 200), xytext=(2008, 700),
            arrowprops=dict(facecolor='gold', arrowstyle='->', lw=1.5),
            fontsize=12, color='gold')

ax.annotate('Rise of Wind Power', xy=(2020, 530), xytext=(2013, 1000),
            arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
            fontsize=12, color='blue')

props = dict(boxstyle='round', facecolor='lightgray', alpha=0.3)
textstr = ('Global efforts have seen\n'
           'a rise in renewable\n'
           'energy consumption.')
ax.text(0.02, 0.95, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

for idx, energy in enumerate(['Solar', 'Wind']):
    ax.annotate(f'{energy_data[idx, 0]}', (2000, energy_data[idx, 0]),
                textcoords="offset points", xytext=(-15, 5), ha='center')
    ax.annotate(f'{energy_data[idx, -1]}', (2020, energy_data[idx, -1] + np.sum(energy_data[:idx, -1])),
                textcoords="offset points", xytext=(-15, -10), ha='center')

plt.tight_layout()
plt.show()