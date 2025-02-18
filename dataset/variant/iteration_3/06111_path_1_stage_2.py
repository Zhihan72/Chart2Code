import matplotlib.pyplot as plt
import numpy as np

# Data for sales numbers
regions = ['North', 'South', 'East', 'West']
reusable_bags = [1200, 950, 1100, 800]
solar_chargers = [750, 850, 920, 700]
bamboo_toothbrushes = [530, 610, 720, 580]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
y_pos = np.arange(len(regions))

# Plot the bars with new colors
ax.barh(y_pos - bar_width, reusable_bags, bar_width, label='Reusable Bags', color='#ff6f61', edgecolor='black', linestyle='-', hatch='/')
ax.barh(y_pos, solar_chargers, bar_width, label='Solar Chargers', color='#6b5b95', edgecolor='black', linestyle='--', hatch='\\')
ax.barh(y_pos + bar_width, bamboo_toothbrushes, bar_width, label='Bamboo Toothbrushes', color='#88b04b', edgecolor='black', linestyle=':', hatch='-')

# Labels and title styles
ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=11)
ax.set_xlabel('Units Sold', fontsize=11)
ax.set_title('EcoTrendz Campaign Effectiveness Across Regions', fontsize=14, fontweight='bold', pad=15)

# Legend with modified position and style
ax.legend(title='Products', loc='lower right', fontsize=9, shadow=True, fancybox=True)

# Remove grid
plt.grid(visible=False)

# Add value labels
for i in range(len(regions)):
    ax.text(reusable_bags[i] + 20, i - bar_width, str(reusable_bags[i]), va='center', color='black', fontsize=9)
    ax.text(solar_chargers[i] + 20, i, str(solar_chargers[i]), va='center', color='black', fontsize=9)
    ax.text(bamboo_toothbrushes[i] + 20, i + bar_width, str(bamboo_toothbrushes[i]), va='center', color='black', fontsize=9)

# Apply tight layout
plt.tight_layout()

# Display the plot
plt.show()