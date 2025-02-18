import matplotlib.pyplot as plt
import numpy as np

regions = ['Amr', 'Eur', 'Asia', 'Afr']
years = ['10', '15', '20']

internet_users = [
    [500, 800, 1100],  # Amr
    [400, 700, 1000],  # Eur
    [1000, 1600, 2300],  # Asia
    [200, 400, 700]  # Afr
]

colors = ['#e63946', '#a8dadc', '#457b9d', '#f1faee']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
ind = np.arange(len(years))

for i, (region, color) in enumerate(zip(regions, colors)):
    bar_positions = ind + i * bar_height
    bars = ax.barh(bar_positions, internet_users[i], bar_height, color=color, label=region)  # Fix: Use internet_users[i] for region data

    # Annotate bars
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}M',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=9, fontstyle='italic')

# Set labels and title
ax.set_ylabel('Year', fontsize=13)
ax.set_yticks(ind + bar_height * (len(regions) - 1) / 2)
ax.set_yticklabels(years, fontsize=13)
ax.set_xlabel('Users (Millions)', fontsize=13)
ax.set_title('Growth of Internet Users', fontsize=16, fontweight='bold')

# Add legend and grid
ax.legend(title='Region', fontsize=11, title_fontsize='13', loc='upper right')
ax.xaxis.grid(True, linestyle='-.', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()