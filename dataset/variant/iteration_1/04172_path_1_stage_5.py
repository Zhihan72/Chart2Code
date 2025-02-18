import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions', 'AstroAdventures']
ticket_sales = [
    [45, 30, 100, 75, 120, 130],
    [20, 65, 50, 35, 105, 90],
    [80, 45, 15, 60, 70, 30],
    [50, 25, 35, 75, 65, 10]
]

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
y_pos = np.arange(len(years))

colors = ['#1E90FF', '#FFD700', '#FF4500', '#9ACD32']

for i, agency_sales in enumerate(ticket_sales):
    marker_shape = ['o', 's', '^', 'D'][i]
    hatch_style = ['', '/', '//', 'x'][i]
    ax.barh(y_pos + i * bar_height, agency_sales, height=bar_height, color=colors[i], edgecolor='gray', hatch=hatch_style)

ax.set_yticks(y_pos + bar_height * 1.5)
ax.set_yticklabels([])  # Remove year labels

# Remove axis titles
ax.set_ylabel('')
ax.set_xlabel('')

# Remove the legend
ax.legend().remove()

for bar_group in ax.containers:
    for bar in bar_group:
        bar.set_label('')  # Remove data labels

ax.grid(False)

plt.tight_layout()

plt.show()