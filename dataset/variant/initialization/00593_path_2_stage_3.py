import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

years = np.arange(2000, 2021)

# Removed north_america data
europe = [5, 6, 7, 9, 10, 12, 14, 16, 19, 21, 23, 26, 29, 31, 34, 36, 39, 41, 44, 47, 50]
asia = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 19, 21, 23, 26, 28, 30, 33, 35, 38]

global_target = [20] * len(years)

fig, ax = plt.subplots(figsize=(14, 8))

# Setting a new set of colors for remaining datagroups
new_palette = sns.color_palette("Set2", 3)

# Removed north_america plot line
ax.plot(years, europe, marker='s', linestyle='-', linewidth=2, color=new_palette[0], label='EU')
ax.plot(years, asia, marker='^', linestyle='-', linewidth=2, color=new_palette[1], label='AS')

ax.plot(years, global_target, linestyle='--', color='gray', label='Global Target 20%')

ax.set_title("Renewable Energy Trends (2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy (%)", fontsize=12)

ax.grid(True, linestyle='--', alpha=0.6)

ax.legend(loc='upper left', fontsize=10, title='Region/Target', title_fontsize=12)

ax.annotate('Paris Agreement', xy=(2015, 50), xytext=(2016, 55),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', color='black')

for i, txt in enumerate(europe):
    if txt == max(europe):
        ax.annotate(f'Peak: {txt}%', xy=(years[i], txt), xytext=(years[i]-2, txt+5),
                    arrowprops=dict(facecolor=new_palette[0], arrowstyle='->'),
                    fontsize=10, color=new_palette[0])

ax2 = ax.twinx()
ax2.set_ylabel('Secondary Metric (Units)', fontsize=12)
ax2.plot(years, [x + 20 for x in asia], linestyle='-', linewidth=1, color='blue', alpha=0.3, label='Imaginary Metric')
ax2.legend(loc='lower right', fontsize=10)

plt.tight_layout()

plt.show()