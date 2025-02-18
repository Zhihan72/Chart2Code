import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

apple = [15, 20, 20, 25, 25, 27, 32, 35, 34, 36, 38]
samsung = [25, 30, 32, 30, 28, 28, 27, 25, 26, 24, 22]
huawei = [10, 12, 15, 16, 18, 20, 22, 24, 22, 20, 19]
xiaomi = [5, 6, 8, 10, 12, 14, 15, 17, 18, 19, 20]
others = [45, 32, 25, 19, 17, 11,  8,  6,  6,  1, 1]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#1E90FF', '#32CD32', '#FFD700', '#606060']

# Line plots
ax.plot(years, apple, label='Fruit Inc.', color=colors[0], marker='o', linewidth=2)
ax.plot(years, samsung, label='Seoul Corp.', color=colors[1], marker='s', linewidth=2)
ax.plot(years, huawei, label='Shenzhen Tech', color=colors[2], marker='D', linewidth=2)
ax.plot(years, xiaomi, label='Tech Giants', color=colors[3], marker='^', linewidth=2)
ax.plot(years, others, label='Misc Brands', color=colors[4], marker='v', linewidth=2)

# Modified title and labels
ax.set_title("Smartphone Market Dynamics (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Timeline (Years)', fontsize=12)
ax.set_ylabel('Share in Market (%)', fontsize=12)

ax.set_ylim(0, 50)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

ax.legend(title='Company Names', fontsize=10, title_fontsize='12')

for year, a, s, h, x, o in zip(years, apple, samsung, huawei, xiaomi, others):
    ax.text(year, a, f'{a}%', ha='center', va='bottom', fontsize=9, color=colors[0])
    ax.text(year, s, f'{s}%', ha='center', va='bottom', fontsize=9, color=colors[1])
    ax.text(year, h, f'{h}%', ha='center', va='bottom', fontsize=9, color=colors[2])
    ax.text(year, x, f'{x}%', ha='center', va='bottom', fontsize=9, color=colors[3])
    ax.text(year, o, f'{o}%', ha='center', va='bottom', fontsize=9, color=colors[4])

plt.tight_layout()
plt.show()