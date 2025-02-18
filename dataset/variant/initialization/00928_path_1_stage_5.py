import matplotlib.pyplot as plt
import numpy as np

regions = ['Am', 'Eur', 'AP']
coffee_types = ['Esp', 'Lat', 'CB']

# Consumption and price data
consumption_data = np.array([
    [25, 55, 20],
    [40, 25, 35],
    [50, 20, 30]
])

price_data = np.array([
    [3.5, 4.0, 3.0],
    [3.2, 2.5, 3.0],
    [4.8, 4.0, 4.5]
])

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
indices = np.arange(len(regions))

# Stack the consumption data
bottom_data = np.zeros(len(regions))
for i, coffee_type in enumerate(coffee_types):
    ax.bar(indices, consumption_data[:, i], bar_width,
           bottom=bottom_data, label=coffee_type, color=colors[i], alpha=0.7)
    bottom_data += consumption_data[:, i]

ax.set_xlabel('Reg', fontsize=12)
ax.set_ylabel('%', fontsize=12)
ax.set_title('Stacked Coffee Cons 2023', fontsize=14, weight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.set_ylim(0, 100)
ax.legend(title='Types', fontsize=9)

plt.tight_layout()
plt.show()