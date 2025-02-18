import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions', 'AstroAdventures']
ticket_sales = [
    [45, 30, 100, 75, 120, 130],  # StarVoyager
    [20, 65, 50, 35, 105, 90],    # CosmoWay
    [80, 45, 15, 60, 70, 30],     # GalacticExpeditions
    [50, 25, 35, 75, 65, 10]      # AstroAdventures
]

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
y_pos = np.arange(len(years))

colors = ['#1E90FF', '#FFD700', '#FF4500', '#9ACD32']

bars = []
for i, agency_sales in enumerate(ticket_sales):
    marker_shape = ['o', 's', '^', 'D'][i]
    hatch_style = ['', '/', '//', 'x'][i]
    bars.append(ax.barh(y_pos + i * bar_height, agency_sales, height=bar_height, color=colors[i], edgecolor='gray', label=agencies[i], hatch=hatch_style))

ax.set_title('Space Tourism Sales (2020-2025)\nAgency Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Years', fontsize=12)
ax.set_xlabel('Sales (Thousands)', fontsize=12)
ax.set_yticks(y_pos + bar_height * 1.5)
ax.set_yticklabels(years)

for bar_group in bars:
    for bar in bar_group:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', fontsize=10)

ax.legend(title='Agencies', loc='upper right', frameon=False, fontsize=10, title_fontsize='12')

ax.grid(False)

plt.tight_layout()

plt.show()