import matplotlib.pyplot as plt
import numpy as np

species = ['Cows', 'Sheep', 'Pigs', 'Goats', 'Chickens']
birth_rates_region_A = np.array([150, 300, 80, 200, 600])
birth_rates_region_B = np.array([180, 250, 110, 150, 750])

weeks = np.arange(1, 5)
weekly_birth_rates_region_A = np.array([
    [30, 70, 15, 50, 150],
    [35, 80, 20, 55, 160],
    [40, 75, 18, 45, 140],
    [45, 75, 27, 50, 150]
])
weekly_birth_rates_region_B = np.array([
    [40, 60, 30, 35, 185],
    [45, 65, 25, 40, 190],
    [50, 60, 35, 30, 185],
    [45, 65, 20, 45, 190]
])

fig, axs = plt.subplots(2, 2, figsize=(15, 12))

axs[0, 0].bar(species, birth_rates_region_A, color='skyblue', edgecolor='black', alpha=0.7, label='Region A')
axs[0, 0].bar(species, birth_rates_region_B, color='lightgreen', edgecolor='black', alpha=0.7, label='Region B', bottom=birth_rates_region_A)
axs[0, 0].set_title('Total Birth Rates of Animals\nin Region A and Region B', fontsize=16, fontweight='bold', pad=20)
axs[0, 0].set_xlabel('Animal Species', fontsize=14)
axs[0, 0].set_ylabel('Birth Rates', fontsize=14)
axs[0, 0].legend(loc='upper left')
axs[0, 0].set_xticks(np.arange(len(species)))
axs[0, 0].set_xticklabels(species, rotation=45, ha='right', fontsize=12)

for i in range(len(species)):
    axs[1, 1].plot(weeks, weekly_birth_rates_region_A[:, i], marker='o', label=species[i])
axs[1, 1].set_title('Weekly Birth Rates\nin Region A', fontsize=16, fontweight='bold', pad=20)
axs[1, 1].set_xlabel('Weeks', fontsize=14)
axs[1, 1].set_ylabel('Birth Rates', fontsize=14)
axs[1, 1].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[1, 1].set_xticks(weeks)
axs[1, 1].grid(True)

for i in range(len(species)):
    axs[1, 0].plot(weeks, weekly_birth_rates_region_B[:, i], marker='o', label=species[i])
axs[1, 0].set_title('Weekly Birth Rates\nin Region B', fontsize=16, fontweight='bold', pad=20)
axs[1, 0].set_xlabel('Weeks', fontsize=14)
axs[1, 0].set_ylabel('Birth Rates', fontsize=14)
axs[1, 0].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[1, 0].set_xticks(weeks)
axs[1, 0].grid(True)

weekly_birth_rate_ratio = weekly_birth_rates_region_B / (weekly_birth_rates_region_A + 1e-6)
for i in range(len(species)):
    axs[0, 1].plot(weeks, weekly_birth_rate_ratio[:, i], marker='x', label=species[i])
axs[0, 1].set_title('Weekly Birth Rates Ratio\n(Region B / Region A)', fontsize=16, fontweight='bold', pad=20)
axs[0, 1].set_xlabel('Weeks', fontsize=14)
axs[0, 1].set_ylabel('Ratio', fontsize=14)
axs[0, 1].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[0, 1].set_xticks(weeks)
axs[0, 1].grid(True)

plt.tight_layout()
plt.show()