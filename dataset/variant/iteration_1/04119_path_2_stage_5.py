import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

# Manually shuffled data to create a random-like alteration while preserving the dimensional structure
battle_royale = np.array([25, 15, 5, 60, 20, 35, 10, 45, 65, 7, 55])
MOBA = np.array([48, 23, 35, 30, 25, 38, 32, 20, 40, 45, 27])
FPS = np.array([40, 36, 28, 33, 20, 22, 15, 30, 18, 25, 23])
sports = np.array([35, 15, 30, 12, 10, 20, 23, 27, 13, 33, 18])
strategy = np.array([22, 24, 10, 9, 26, 20, 16, 18, 12, 14, 8])

# Recalculating total_engagement with the shuffled data
total_engagement = battle_royale + MOBA + FPS + sports + strategy

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, total_engagement, marker='o', color='#ff7f0e', linestyle='-', linewidth=2)
ax.fill_between(years, 0, total_engagement, color='#ffcc66', alpha=0.5)

plt.tight_layout()
plt.show()