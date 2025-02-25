import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['Americas', 'Europe', 'Asia', 'Africa', 'Oceania']
years = ['2020', '2015', '2010']

# Internet users data (in millions) for each region over the years
internet_users = [
    [500, 800, 1100],  # Americas
    [400, 700, 1000],  # Europe
    [1000, 1600, 2300], # Asia
    [200, 400, 700],    # Africa
    [50, 100, 200]      # Oceania
]

# Shuffled Colors for each region
colors = ['#48cae4', '#caf0f8', '#0077b6', '#90e0ef', '#00b4d8']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
ind = np.arange(len(years))

# Plotting the bars with shuffled colors
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

ax.set_xlabel('Decade', fontsize=12)
ax.set_xticks(ind + bar_width * (len(regions) - 1) / 2)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Digital Population (in millions)', fontsize=12)
ax.set_title('User Uprise Globally (2010-2020)', fontsize=16, fontweight='bold')

ax.legend(title='Continents', fontsize=10, title_fontsize='12', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()