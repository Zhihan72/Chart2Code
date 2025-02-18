import matplotlib.pyplot as plt
import numpy as np

# Define the species and data points for birth rates
species = ['Cows', 'Sheep', 'Pigs', 'Goats', 'Chickens', 'Ducks']
birth_rates_region_A = np.array([150, 300, 80, 200, 600, 120])
birth_rates_region_B = np.array([180, 250, 110, 150, 750, 100])

# Create weekly birth rates data (simplified for illustration)
weeks = np.arange(1, 5)

weekly_birth_rates_region_A = np.array([
    [30, 70, 15, 50, 150, 30],  # Week 1
    [35, 80, 20, 55, 160, 25],  # Week 2
    [40, 75, 18, 45, 140, 35],  # Week 3
    [45, 75, 27, 50, 150, 30]   # Week 4
])

weekly_birth_rates_region_B = np.array([
    [40, 60, 30, 35, 185, 25],  # Week 1
    [45, 65, 25, 40, 190, 20],  # Week 2
    [50, 60, 35, 30, 185, 20],  # Week 3
    [45, 65, 20, 45, 190, 35]   # Week 4
])

# Setup figure and axis
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# Define a single color for all data groups
single_color = 'teal'

# Overall birth rates in Region A and B
axs[0, 0].bar(species, birth_rates_region_A, color=single_color, edgecolor='black', alpha=0.7, label='Region A')
axs[0, 0].bar(species, birth_rates_region_B, color=single_color, edgecolor='black', alpha=0.7, label='Region B', bottom=birth_rates_region_A)
axs[0, 0].set_title('Total Birth Rates of Animals\nin Region A and Region B', fontsize=16, fontweight='bold', pad=20)
axs[0, 0].set_xlabel('Animal Species', fontsize=14)
axs[0, 0].set_ylabel('Birth Rates', fontsize=14)
axs[0, 0].legend(loc='upper left')
axs[0, 0].set_xticks(np.arange(len(species)))
axs[0, 0].set_xticklabels(species, rotation=45, ha='right', fontsize=12)

# Weekly birth rates in Region A
for i in range(len(species)):
    axs[0, 1].plot(weeks, weekly_birth_rates_region_A[:, i], marker='o', color=single_color, label=species[i])
axs[0, 1].set_title('Weekly Birth Rates\nin Region A', fontsize=16, fontweight='bold', pad=20)
axs[0, 1].set_xlabel('Weeks', fontsize=14)
axs[0, 1].set_ylabel('Birth Rates', fontsize=14)
axs[0, 1].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[0, 1].set_xticks(weeks)
axs[0, 1].grid(True)

# Weekly birth rates in Region B
for i in range(len(species)):
    axs[1, 0].plot(weeks, weekly_birth_rates_region_B[:, i], marker='o', color=single_color, label=species[i])
axs[1, 0].set_title('Weekly Birth Rates\nin Region B', fontsize=16, fontweight='bold', pad=20)
axs[1, 0].set_xlabel('Weeks', fontsize=14)
axs[1, 0].set_ylabel('Birth Rates', fontsize=14)
axs[1, 0].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[1, 0].set_xticks(weeks)
axs[1, 0].grid(True)

# Comparison of weekly birth rates ratio (Region B / Region A)
weekly_birth_rate_ratio = weekly_birth_rates_region_B / (weekly_birth_rates_region_A + 1e-6)  # Avoid division by zero
for i in range(len(species)):
    axs[1, 1].plot(weeks, weekly_birth_rate_ratio[:, i], marker='x', color=single_color, label=species[i])
axs[1, 1].set_title('Weekly Birth Rates Ratio\n(Region B / Region A)', fontsize=16, fontweight='bold', pad=20)
axs[1, 1].set_xlabel('Weeks', fontsize=14)
axs[1, 1].set_ylabel('Ratio', fontsize=14)
axs[1, 1].legend(title='Species', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)
axs[1, 1].set_xticks(weeks)
axs[1, 1].grid(True)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()