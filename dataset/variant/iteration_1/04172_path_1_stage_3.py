import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions', 'AstroAdventures']
ticket_sales = [
    [45, 30, 100, 75, 120, 130],  # StarVoyager (shuffled)
    [20, 65, 50, 35, 105, 90],    # CosmoWay (shuffled)
    [80, 45, 15, 60, 70, 30],     # GalacticExpeditions (shuffled)
    [50, 25, 35, 75, 65, 10]      # AstroAdventures (shuffled)
]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x_pos = np.arange(len(years))

# New colors for each agency
colors = ['#1E90FF', '#FFD700', '#FF4500', '#9ACD32']

bars = []
for i, agency_sales in enumerate(ticket_sales):
    marker_shape = ['o', 's', '^', 'D'][i]
    hatch_style = ['', '/', '//', 'x'][i]
    bars.append(ax.bar(x_pos + i * bar_width, agency_sales, width=bar_width, color=colors[i], edgecolor='gray', label=agencies[i], hatch=hatch_style))

ax.set_title('Space Tourism Sales (2020-2025)\nAgency Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Sales (Thousands)', fontsize=12)
ax.set_xticks(x_pos + bar_width * 1.5)
ax.set_xticklabels(years, rotation=30)

for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', fontsize=10)

ax.legend(title='Agencies', loc='upper right', frameon=False, fontsize=10, title_fontsize='12')

ax.grid(False)

plt.tight_layout()

plt.show()