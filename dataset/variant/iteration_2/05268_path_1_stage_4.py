import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

socialgram_users = [200, 410, 110, 75, 500, 50, 600, 150, 330, 260]
chatbuzz_users = [100, 430, 170, 60, 280, 80, 520, 220, 350, 130]
imageshare_users = [70, 190, 140, 30, 320, 45, 490, 250, 400, 100]

fig, ax = plt.subplots(figsize=(14, 8))

# Change colors, marker types, and line styles
ax.plot(years, socialgram_users, label='SGram', marker='v', linestyle='--', linewidth=2.0, color='green', alpha=0.8)
ax.plot(years, chatbuzz_users, label='CBuzz', marker='>', linestyle='-.', linewidth=2.0, color='red', alpha=0.8)
ax.plot(years, imageshare_users, label='IShare', marker='<', linestyle=':', linewidth=2.0, color='purple', alpha=0.8)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Users (millions)', fontsize=12)
ax.set_title('User Growth from 2013 to 2022', fontsize=16, fontweight='bold')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 800, 100))
# Modify grid style
ax.grid(True, linestyle='-', alpha=0.3)
# Keep all spines visible and add varying colors
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')
ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.show()