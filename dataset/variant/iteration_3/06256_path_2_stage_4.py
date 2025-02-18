import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

apple = [15, 25, 20, 25, 32, 20, 36, 34, 38, 27, 35]
samsung = [32, 30, 25, 28, 30, 27, 24, 26, 22, 28, 25]
huawei = [12, 15, 16, 18, 20, 10, 19, 22, 24, 22, 20]
xiaomi = [6, 8, 14, 12, 10, 15, 20, 17, 19, 18, 5]
others = [32, 8, 6, 19, 11, 17, 1, 6, 45, 25, 1]

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled colors
colors = ['#606060', '#FF5733', '#1E90FF', '#32CD32', '#FFD700']

ax.plot(years, apple, color=colors[0], marker='o', linewidth=2)
ax.plot(years, samsung, color=colors[1], marker='s', linewidth=2)
ax.plot(years, huawei, color=colors[2], marker='D', linewidth=2)
ax.plot(years, xiaomi, color=colors[3], marker='^', linewidth=2)
ax.plot(years, others, color=colors[4], marker='v', linewidth=2)

ax.set_title("Smartphone Market Share (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('% Share', fontsize=12)

ax.set_ylim(0, 50)

for year, a, s, h, x, o in zip(years, apple, samsung, huawei, xiaomi, others):
    ax.text(year, a, f'{a}', ha='center', va='bottom', fontsize=9, color=colors[0])
    ax.text(year, s, f'{s}', ha='center', va='bottom', fontsize=9, color=colors[1])
    ax.text(year, h, f'{h}', ha='center', va='bottom', fontsize=9, color=colors[2])
    ax.text(year, x, f'{x}', ha='center', va='bottom', fontsize=9, color=colors[3])
    ax.text(year, o, f'{o}', ha='center', va='bottom', fontsize=9, color=colors[4])

plt.tight_layout()

plt.show()