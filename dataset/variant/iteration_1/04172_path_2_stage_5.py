import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions']
ticket_sales = [
    [30, 54, 75, 100, 120, 130],  # StarVoyager
    [20, 35, 50, 65, 90, 105],    # CosmoWay
    [15, 30, 45, 60, 70, 80]      # GalacticExpeditions
]

fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.2
y_pos = np.arange(len(years))

single_color = '#4682B4'  # Consistent color for all bars

for i, agency_sales in enumerate(ticket_sales):
    ax.barh(y_pos + i * bar_height, agency_sales, height=bar_height, color=single_color, edgecolor='grey')

ax.set_yticks(y_pos + bar_height)
ax.set_yticklabels(years)

ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_color('#FF6347')

plt.tight_layout()
plt.show()