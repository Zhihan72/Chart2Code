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
hydro = np.array([
    30, 35, 40, 45, 50, 55, 60, 70, 80, 95, 
    115, 135, 160, 190, 225, 265, 310, 360, 420, 490, 570
])

energy_data = np.vstack([solar, wind, hydro])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#00BFFF', '#32CD32', '#FFD700']  # Randomly altered color order
labels = ['Wind Power', 'Solar Power', 'Hydroelectric Power']  # Shuffled labels

ax.stackplot(years, energy_data, labels=labels, colors=colors, alpha=0.75)

ax.set_title("Renewable Energy Adoption Overview\n(2000-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Adoption (Gigawatts)', fontsize=14)
ax.legend(loc='upper right', fontsize=12, title='Energy Source', frameon=True)
ax.grid(linestyle=':', alpha=0.7)

# Changed the markers in annotations and reduced redundant annotation
ax.annotate('Solar Peak', xy=(2015, 620), xytext=(2010, 900),
            arrowprops=dict(facecolor='green', arrowstyle='-|>', lw=1.5),
            fontsize=12, color='green')

props = dict(boxstyle='square', facecolor='lightgrey', alpha=0.25)
textstr = ('Significant growth in renewable\n'
           'energy adoption observed globally.')
ax.text(0.02, 0.05, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='bottom', bbox=props)

for idx, energy in enumerate(labels):
    ax.annotate(f'{energy_data[idx, 0]}', (2000, energy_data[idx, 0]),
                textcoords="offset points", xytext=(-10, 5), ha='center')
    ax.annotate(f'{energy_data[idx, -1]}', (2020, energy_data[idx, -1] + np.sum(energy_data[:idx, -1])),
                textcoords="offset points", xytext=(-10, -10), ha='center')

plt.tight_layout()
plt.show()