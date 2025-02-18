import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

# Data points are manually shuffled to preserve original dimensions
socialgram_users = [200, 410, 110, 75, 500, 50, 600, 150, 330, 260]
chatbuzz_users = [100, 430, 170, 60, 280, 80, 520, 220, 350, 130]
imageshare_users = [70, 190, 140, 30, 320, 45, 490, 250, 400, 100]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, socialgram_users, label='SGram', marker='o', linestyle='-', linewidth=2.5, color='blue', alpha=0.7)
ax.plot(years, chatbuzz_users, label='CBuzz', marker='s', linestyle='-', linewidth=2.5, color='green', alpha=0.7)
ax.plot(years, imageshare_users, label='IShare', marker='^', linestyle='-', linewidth=2.5, color='orange', alpha=0.7)

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Users (M)', fontsize=12)
ax.set_title('User Growth: 2013-2022', fontsize=16, fontweight='bold')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 800, 100))
ax.grid(True, linestyle='--', alpha=0.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()