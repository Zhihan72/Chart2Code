import matplotlib.pyplot as plt
import numpy as np

species = ['Cows', 'Sheep', 'Pigs', 'Goats', 'Chickens', 'Ducks']
birth_rates_A = np.array([150, 300, 80, 200, 600, 120])
birth_rates_B = np.array([180, 250, 110, 150, 750, 100])
birth_rates_C = np.array([130, 270, 90, 220, 500, 140])  # New data series for Region C

weeks = np.arange(1, 5)

weekly_birth_rates_A = np.array([
    [30, 70, 15, 50, 150, 30],
    [35, 80, 20, 55, 160, 25],
    [40, 75, 18, 45, 140, 35],
    [45, 75, 27, 50, 150, 30]
])

weekly_birth_rates_C = np.array([  # New weekly data
    [20, 60, 12, 60, 130, 35],
    [30, 90, 25, 65, 155, 30],
    [35, 85, 19, 40, 135, 45],
    [50, 70, 28, 60, 160, 25]
])

birth_rate_ratio = (weekly_birth_rates_A + weekly_birth_rates_C) / (weekly_birth_rates_A + weekly_birth_rates_C + 1e-6)

fig, axs = plt.subplots(2, figsize=(10, 12))

colors = ['teal', 'orange']  # Different colors for each region

# Total Birth Rates
axs[0].bar(species, birth_rates_A, color=colors[0], edgecolor='black', alpha=0.7, label='Region A')
axs[0].bar(species, birth_rates_B, color=colors[0], edgecolor='black', alpha=0.7, label='Region B', bottom=birth_rates_A)
axs[0].bar(species, birth_rates_C, color=colors[1], edgecolor='black', alpha=0.7, label='Region C', bottom=birth_rates_A + birth_rates_B)
axs[0].set_title('Total Birth Rates (A, B & C)', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Species', fontsize=12)
axs[0].set_ylabel('Rates', fontsize=12)
axs[0].legend(loc='upper left')
axs[0].set_xticks(np.arange(len(species)))
axs[0].set_xticklabels(species, rotation=45, ha='right', fontsize=10)

# Weekly Birth Rates Ratio
for i in range(len(species)):
    axs[1].plot(weeks, birth_rate_ratio[:, i], marker='x', color=colors[i % 2], label=species[i] if i < 3 else "")  # Added alternate coloring
axs[1].set_title('Weekly Ratio ((A+C)/All)', fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel('Weeks', fontsize=12)
axs[1].set_ylabel('Ratio', fontsize=12)
axs[1].legend(title='Species', fontsize=9, edgecolor='gray', framealpha=0.7)
axs[1].set_xticks(weeks)
axs[1].grid(True)

plt.tight_layout()
plt.show()