import matplotlib.pyplot as plt
import numpy as np

regions = ['Amr', 'Eur', 'Asia', 'Afr']
years = ['10', '15', '20']

internet_users = [
    [500, 800, 1100],  
    [400, 700, 1000],  
    [1000, 1600, 2300],
    [200, 400, 700] 
]

# New set of colors to use for plotting
colors = ['#e63946', '#f1faee', '#a8dadc', '#457b9d']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
ind = np.arange(len(years))

for i, (region, color) in enumerate(zip(regions, colors)):
    bar_positions = ind + i * bar_width
    bars = ax.bar(bar_positions, internet_users[i], bar_width, color=color, label=region)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Yr', fontsize=12)
ax.set_xticks(ind + bar_width * (len(regions) - 1) / 2)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Users (M)', fontsize=12)
ax.set_title('Internet Users Growth', fontsize=16, fontweight='bold')

ax.legend(title='Regions', fontsize=10, title_fontsize='12', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()