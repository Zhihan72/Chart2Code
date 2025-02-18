import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
age_groups = ["Children", "Teens", "20s", "30s", "40s", "50+", "60+", "Middle-aged"]

children = [2, 3, 5, 7, 10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 85]
teens = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 88, 90, 92, 94, 95, 96, 97]
twenties = [10, 15, 25, 35, 50, 55, 60, 65, 70, 75, 80, 82, 83, 85, 86, 87, 88, 89, 90, 90, 90]
thirties = [5, 8, 12, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 68, 70, 72, 74, 76, 78, 80, 82]
forties = [3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 63, 64, 65, 66, 67, 68, 70]
fifties_plus = [1, 2, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 48, 50, 52, 54, 56, 58, 60]
seniors = [0, 1, 2, 3, 4, 5, 6, 8, 10, 13, 15, 17, 19, 21, 23, 24, 25, 26, 27, 28, 30]
middle_aged = [4, 7, 10, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 70, 73, 76, 78, 80, 83]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#8A2BE2', '#E69F00', '#56B4E9', '#FF0000', '#00A2FF', '#009E73', '#D55E00', '#FF69B4']
markers = ['o', '^', 'v', 'x', 's', 'o', 'D', 'p']
linestyles = ['--', '-', '--', '-.', ':', '-', '--', '-.']

for data, name, color, marker, linestyle in zip(
    [children, teens, twenties, thirties, forties, fifties_plus, seniors, middle_aged], 
    age_groups, colors, markers, linestyles):
    ax.plot(years, data, label=name, color=color, marker=marker, linewidth=2, linestyle=linestyle)
    ax.annotate(f'{data[-1]}%', xy=(years[-1], data[-1]), xytext=(5, -5), textcoords='offset points', ha='center', fontsize=9, color=color)

ax.set_title('Internet Usage by Age (2000-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage (%)', fontsize=12)

ax.legend(title='Ages', title_fontsize='13', loc='upper right', frameon=True, framealpha=0.5, fancybox=True)
ax.grid(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlim(2000, 2020)
ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()