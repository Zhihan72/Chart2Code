import matplotlib.pyplot as plt
import numpy as np

consumption_percentages = [25, 20, 15, 25, 15]
single_color = '#6db33f'

years = ['2018', '2019', '2020', '2021', '2022']
trend_data = [
    [21, 24, 23, 27, 32],
    [15, 18, 20, 21, 19],
    [12, 15, 16, 14, 14],
    [23, 25, 22, 26, 24],
    [13, 11, 15, 16, 14]
]

fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

wedges, _ , autotexts = ax.pie(
    consumption_percentages, colors=[single_color] * len(consumption_percentages),
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.3)
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

ax2 = ax.twinx()

x = np.arange(len(years))
width = 0.15

for i in range(len(trend_data)):
    ax2.bar(x + i * width, trend_data[i], width, color=single_color, alpha=0.6)

ax2.set_xticks(x + width * 2)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylim(0, 35)

plt.tight_layout()
plt.show()