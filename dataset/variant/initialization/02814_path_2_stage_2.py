import matplotlib.pyplot as plt
import numpy as np

decades = ['70s', '80s', '90s', '00s', '10s']
cities = ['Harm', 'Innov', 'Bal']

solar_energy = np.array([
    [5, 10, 15, 20, 25],  # Harmony
    [3, 8, 14, 22, 30],   # Innovation
    [4, 7, 12, 18, 24]    # Balance
])

wind_energy = np.array([
    [10, 12, 15, 20, 30],  # Harmony
    [6, 10, 14, 18, 24],   # Innovation
    [5, 9, 13, 17, 22]     # Balance
])

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(decades, solar_energy[0], color='#FFD700', alpha=0.6, label='Solar')
ax.fill_between(decades, wind_energy[0], color='#4682B4', alpha=0.6, label='Wind')

ax.plot(decades, solar_energy[0], color='#FFD700', linewidth=2)
ax.plot(decades, wind_energy[0], color='#4682B4', linewidth=2)

ax.set_title("Energy in Harmony", fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Usage (Units)', fontsize=12)
ax.legend(loc='upper left', title="Types", fontsize=10)

ax.set_xticks(decades)
ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)

for i, energy in enumerate([solar_energy, wind_energy]):
    ax.annotate(
        str(energy[0][-1]),
        xy=(decades[-1], energy[0][-1]),
        xytext=(10, -10 * i),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', lw=1.5),
        fontsize=10,
        color='black'
    )

plt.tight_layout()
plt.show()