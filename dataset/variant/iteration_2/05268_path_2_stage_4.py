import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

# Random shuffling within the preserved structure
socialgram_users = [
    75, 110, 260, 150, 330, 200, 410, 50, 600, 500
]

chatbuzz_users = [
    130, 100, 60, 220, 430, 280, 350, 80, 170, 520
]

imageshare_users = [
    100, 45, 250, 320, 30, 400, 140, 70, 190, 490
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, socialgram_users, marker='o', linestyle='-', linewidth=2.5, color='red', alpha=0.7)
ax.plot(years, chatbuzz_users, marker='s', linestyle='-', linewidth=2.5, color='red', alpha=0.7)
ax.plot(years, imageshare_users, marker='^', linestyle='-', linewidth=2.5, color='red', alpha=0.7)

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Users (M)', fontsize=12)
ax.set_title('Social Media User Growth (2013-2022)', fontsize=16, fontweight='bold')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 800, 100))

# Hide top and right spines
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()