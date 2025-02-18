import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
battle_royale = np.array([5, 7, 10, 15, 20, 25, 35, 45, 55, 60, 65])
MOBA = np.array([20, 23, 25, 27, 30, 32, 35, 38, 40, 45, 48])
FPS = np.array([15, 18, 20, 22, 23, 25, 28, 30, 33, 36, 40])
sports = np.array([10, 12, 13, 15, 18, 20, 23, 27, 30, 33, 35])
strategy = np.array([8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26])

total_engagement = battle_royale + MOBA + FPS + sports + strategy

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, total_engagement, marker='o', color='#ff7f0e', linestyle='-', linewidth=2)
ax.fill_between(years, 0, total_engagement, color='#ffcc66', alpha=0.5)
ax.set_title('Total Esports Engagement (2015-2025)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Total Engagement (Millions)', fontsize=14)

plt.tight_layout()
plt.show()