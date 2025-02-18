import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions', 'AstroAdventures']
ticket_sales = [
    [30, 54, 75, 100, 120, 130],  # StarVoyager
    [20, 35, 50, 65, 90, 105],    # CosmoWay
    [15, 30, 45, 60, 70, 80],     # GalacticExpeditions
    [10, 25, 35, 50, 65, 75]      # AstroAdventures
]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x_pos = np.arange(len(years))

# New colors for each agency
colors = ['#1E90FF', '#FFD700', '#FF4500', '#9ACD32']

bars = []
for i, agency_sales in enumerate(ticket_sales):
    marker_shape = ['o', 's', '^', 'D'][i]  # Different marker shapes
    hatch_style = ['', '/', '//', 'x'][i]   # Different hatch styles
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