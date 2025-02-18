import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A fictional company, "EcoTrendz," is evaluating its marketing campaign effectiveness
# across different regions in promoting eco-friendly products. The campaign focuses on
# promoting three main eco-friendly products: Reusable Bags, Solar Chargers, and 
# Bamboo Toothbrushes in four different regions: North, South, East, and West.

# Data: Sales numbers (in units sold) for each product across different regions
regions = ['North', 'South', 'East', 'West']
reusable_bags = [1200, 950, 1100, 800]
solar_chargers = [750, 850, 920, 700]
bamboo_toothbrushes = [530, 610, 720, 580]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.25
y_pos = np.arange(len(regions))

# Plot the bars for each product in each region
ax.barh(y_pos - bar_width, reusable_bags, bar_width, label='Reusable Bags', color='#6a994e')
ax.barh(y_pos, solar_chargers, bar_width, label='Solar Chargers', color='#a7c957')
ax.barh(y_pos + bar_width, bamboo_toothbrushes, bar_width, label='Bamboo Toothbrushes', color='#f2e8cf')

# Set the labels and title
ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=12)
ax.set_xlabel('Units Sold', fontsize=12)
ax.set_title('EcoTrendz Marketing Campaign Effectiveness\nAcross Different Regions in Q1 2023', fontsize=14, fontweight='bold', pad=20)

# Add a legend
ax.legend(title='Products', loc='upper right', fontsize=10)

# Add value labels to each bar
for i in range(len(regions)):
    ax.text(reusable_bags[i] + 10, i - bar_width, str(reusable_bags[i]), va='center', color='black', fontsize=10)
    ax.text(solar_chargers[i] + 10, i, str(solar_chargers[i]), va='center', color='black', fontsize=10)
    ax.text(bamboo_toothbrushes[i] + 10, i + bar_width, str(bamboo_toothbrushes[i]), va='center', color='black', fontsize=10)

# Enhance plot layout
plt.grid(visible=True, which='major', axis='x', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()