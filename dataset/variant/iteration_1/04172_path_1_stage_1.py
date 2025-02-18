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
colors = ['#FF4500', '#1E90FF', '#9ACD32', '#FFD700']

# Creating the bar chart
bars = []
for i, agency_sales in enumerate(ticket_sales):
    bars.append(ax.bar(x_pos + i * bar_width, agency_sales, width=bar_width, color=colors[i], label=agencies[i], edgecolor='black'))

ax.set_title('Space Tourism Ticket Sales Growth (2020-2025)\nA Comparative Insight by Agency', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Ticket Sales (Thousands)', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos + bar_width * 1.5)
ax.set_xticklabels(years)

for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.legend(title='Space Agencies', loc='upper left', frameon=True, fontsize=10, title_fontsize='12')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()