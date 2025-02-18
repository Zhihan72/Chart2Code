import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility according to the task requirements
np.random.seed(0)

years = np.arange(2015, 2026)

# Original data for each region
north_america = np.array([100, 150, 230, 330, 450, 580, 730, 890, 1070, 1260, 1460])
europe = np.array([80, 120, 200, 290, 410, 550, 720, 900, 1100, 1310, 1530])
asia = np.array([60, 90, 170, 270, 390, 530, 690, 870, 1070, 1290, 1520])
other_regions = np.array([20, 35, 60, 95, 140, 200, 280, 380, 500, 640, 800])

# Randomly alter data within a small range to preserve structure
# For instance, making a slight 10% random perturbation
north_america += np.random.randint(-15, 16, size=north_america.shape)
europe += np.random.randint(-12, 13, size=europe.shape)
asia += np.random.randint(-10, 11, size=asia.shape)
other_regions += np.random.randint(-2, 3, size=other_regions.shape)

data = np.vstack([north_america, europe, asia, other_regions])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, labels=['North America', 'Asia', 'Europe', 'Other Regions'],
             colors=['#2ca02c', '#d62728', '#ff7f0e', '#1f77b4'], alpha=0.85, edgecolor='gray', linewidth=1.5)

ax.set_title('EV Adoption Growth by Areas\nfrom 2015 to 2025', fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Year', fontsize=13, style='italic')
ax.set_ylabel('EVs Count (thousands)', fontsize=13, style='italic')

ax.legend(loc='upper left', fontsize=11, shadow=True, fancybox=True)
ax.grid(axis='y', linestyle=':', linewidth=1, alpha=0.6)
plt.xticks(years, rotation=30)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tight_layout()

plt.show()