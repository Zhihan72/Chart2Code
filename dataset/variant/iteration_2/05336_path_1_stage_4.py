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

colors = ['#e63946', '#a8dadc', '#457b9d', '#f1faee']  # Rearrange color order

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
ind = np.arange(len(years))

# Alter the order of markers
markers = ['o', 'v', 's', '^']

for i, (region, color, marker) in enumerate(zip(regions, colors, markers)):
    bar_positions = ind + i * bar_width
    bars = ax.bar(bar_positions, internet_users[i], bar_width, color=color, label=region, hatch=marker)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontstyle='italic')  # Change font style

ax.set_xlabel('Year', fontsize=13)  # Change label
ax.set_xticks(ind + bar_width * (len(regions) - 1) / 2)
ax.set_xticklabels(years, fontsize=13)
ax.set_ylabel('Users (Millions)', fontsize=13)  # Change label
ax.set_title('Growth of Internet Users', fontsize=16, fontweight='bold')

ax.legend(title='Region', fontsize=11, title_fontsize='13', loc='upper right')  # Change legend location
ax.yaxis.grid(True, linestyle='-.', alpha=0.5)  # Change grid style
ax.spines['top'].set_visible(False)  # Remove top border
ax.spines['right'].set_visible(False)  # Remove right border

plt.tight_layout()
plt.show()