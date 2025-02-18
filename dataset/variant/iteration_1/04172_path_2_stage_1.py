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

# Alter styling elements
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
x_pos = np.arange(len(years))

# Change colors and marker styles
colors = ['#DA70D6', '#20B2AA', '#FF4500', '#6A5ACD']
markers = ['o', 's', 'D', '^']
linestyle = ['-', '--', '-.', ':']

bars = []
for i, agency_sales in enumerate(ticket_sales):
    bars.append(ax.bar(x_pos + i * bar_width, agency_sales, width=bar_width, color=colors[i], edgecolor='grey'))

ax.set_title('Space Tourism Ticket Sales Growth (2020-2025)', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Ticket Sales (Thousands)', fontsize=12)
ax.set_xticks(x_pos + bar_width * 1.5)
ax.set_xticklabels(years)

for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom', fontsize=10)

# Alter legend style
ax.legend(agencies, loc='upper right', frameon=False, fontsize=10)

# Change grid style
ax.yaxis.grid(True, linestyle=linestyle[1], alpha=0.5)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_color('#FF6347')

plt.tight_layout()
plt.show()