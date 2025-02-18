import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

socialgram_users = [
    50, 75, 110, 150, 200, 260, 330, 410, 500, 600,
]

chatbuzz_users = [
    60, 80, 100, 130, 170, 220, 280, 350, 430, 520,
]

imageshare_users = [
    30, 45, 70, 100, 140, 190, 250, 320, 400, 490,
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, socialgram_users, marker='o', linestyle='-', linewidth=2.5, color='red', alpha=0.7)
ax.plot(years, chatbuzz_users, marker='s', linestyle='-', linewidth=2.5, color='red', alpha=0.7)
ax.plot(years, imageshare_users, marker='^', linestyle='-', linewidth=2.5, color='red', alpha=0.7)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Users (Millions)', fontsize=12)
ax.set_title('User Growth Trends of Major Social Media Platforms (2013-2022)', fontsize=16, fontweight='bold')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 800, 100))

# Remove the grid
# ax.grid(True, linestyle='--', alpha=0.6)

# Hide top and right spines (borders) are already hidden
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Remove the legend
# ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()