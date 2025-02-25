import matplotlib.pyplot as plt
import numpy as np

species = ['Cows', 'Sheep', 'Pigs', 'Goats', 'Chickens', 'Ducks']
birth_rates_region_A = np.array([150, 300, 80, 200, 600, 120])
birth_rates_region_B = np.array([180, 250, 110, 150, 750, 100])

weeks = np.arange(1, 5)

weekly_birth_rates_region_A = np.array([
    [30, 70, 15, 50, 150, 30],
    [35, 80, 20, 55, 160, 25],
    [40, 75, 18, 45, 140, 35],
    [45, 75, 27, 50, 150, 30]
])

weekly_birth_rate_ratio = weekly_birth_rates_region_A / (weekly_birth_rates_region_A + 1e-6)

fig, axs = plt.subplots(2, figsize=(10, 12))

single_color = 'teal'

# Overall birth rates in Region A and B
axs[0].bar(species, birth_rates_region_A, color=single_color, edgecolor='black', alpha=0.7, label='Region A')
axs[0].bar(species, birth_rates_region_B, color=single_color, edgecolor='black', alpha=0.7, label='Region B', bottom=birth_rates_region_A)
axs[0].set_title('Total Birth Rates of Animals\nin Region A and Region B', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Animal Species', fontsize=14)
axs[0].set_ylabel('Birth Rates', fontsize=14)
axs[0].legend(loc='upper left')
axs[0].set_xticks(np.arange(len(species)))
axs[0].set_xticklabels(species, rotation=45, ha='right', fontsize=12)

# Comparison of weekly birth rates ratio (Region B / Region A)
for i in range(len(species)):
    axs[1].plot(weeks, weekly_birth_rate_ratio[:, i], marker='x', color=single_color, label=species[i])
axs[1].set_title('Weekly Birth Rates Ratio\n(Region B / Region A)', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Weeks', fontsize=14)
axs[1].set_ylabel('Ratio', fontsize=14)
axs[1].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[1].set_xticks(weeks)
axs[1].grid(True)

plt.tight_layout()
plt.show()