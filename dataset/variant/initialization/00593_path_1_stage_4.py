import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

years = np.arange(2000, 2021)

north_america = [5, 3, 4, 2, 7, 14, 6, 8, 10, 12, 13, 17, 16, 5, 18, 19, 20, 22, 23, 25, 27]
europe = [9, 6, 7, 12, 10, 5, 14, 16, 34, 21, 23, 26, 29, 31, 19, 36, 39, 41, 44, 47, 50]
asia = [4, 2, 2, 3, 1, 5, 6, 8, 14, 12, 10, 16, 19, 21, 26, 23, 28, 30, 33, 35, 38]

global_target = [20] * len(years)

fig, ax = plt.subplots(figsize=(14, 8))

single_color = 'blue'

ax.plot(years, north_america, marker='x', linestyle='--', linewidth=2, color=single_color, label='N. Amer.')
ax.plot(years, europe, marker='d', linestyle=':', linewidth=2, color=single_color, label='EU')
ax.plot(years, asia, marker='p', linestyle='-.', linewidth=2, color=single_color, label='ASIA')
ax.plot(years, global_target, linestyle='-', linewidth=2, color='gray', label='Global Aim')

ax.set_title("Renewable Energy Trends\n(2000-20)", fontsize=16, fontweight='bold')
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Renewable Usage (%)", fontsize=12)

ax.grid(True, linestyle='-.', alpha=0.9, color='blue')
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_color('none')

ax.legend(loc='lower right', fontsize=10, title='Areas & Goals', title_fontsize=12)

ax.annotate('Paris Accord', xy=(2015, 50), xytext=(2016, 53),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', color='black')

for i, txt in enumerate(europe):
    if txt == max(europe):
        ax.annotate(f'High: {txt}%', xy=(years[i], txt), xytext=(years[i]-3, txt+5),
                    arrowprops=dict(facecolor=single_color, arrowstyle='->'),
                    fontsize=10, color=single_color)

ax2 = ax.twinx()
ax2.set_ylabel('Sample Secondary Index', fontsize=12)
ax2.plot(years, [x + 20 for x in asia], linestyle='--', linewidth=1, color='red', alpha=0.3, label='Sample Metric')
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()