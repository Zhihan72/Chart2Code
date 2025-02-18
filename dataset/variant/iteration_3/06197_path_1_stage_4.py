import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plastic_recycling = [8.5, 8.7, 9.1, 9.5, 9.7, 10.0, 9.8, 9.9, 10.3, 10.5, 10.7, 11.0]
glass_recycling = [5.0, 5.1, 5.2, 5.4, 5.6, 5.7, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5]
metal_recycling = [3.0, 3.1, 3.2, 3.4, 3.5, 3.7, 3.6, 3.8, 4.0, 4.1, 4.3, 4.4]
paper_recycling = [12.0, 12.3, 12.5, 13.0, 13.2, 13.5, 13.6, 13.8, 14.0, 14.3, 14.5, 14.8]

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))  # Changed to 2 rows and 1 column

bar_width = 0.2
x_indexes = np.arange(len(months))

# Grouped bar chart for monthly recycling rates
ax[0].bar(x_indexes - 1.5 * bar_width, plastic_recycling, width=bar_width, color='#33FF57', alpha=0.8, label='Plastic')
ax[0].bar(x_indexes - 0.5 * bar_width, glass_recycling, width=bar_width, color='#FFD700', alpha=0.8, label='Glass')
ax[0].bar(x_indexes + 0.5 * bar_width, metal_recycling, width=bar_width, color='#FF5733', alpha=0.8, label='Metal')
ax[0].bar(x_indexes + 1.5 * bar_width, paper_recycling, width=bar_width, color='#3357FF', alpha=0.8, label='Paper')

ax[0].set_xticks(x_indexes)
ax[0].set_xticklabels(months)
ax[0].set_title('Monthly Recycling Rates')
ax[0].legend()
ax[0].grid(True, linestyle='--', alpha=0.7)

# Stacked bar chart for percentage contributions
total_recycling = np.array(plastic_recycling) + np.array(glass_recycling) + np.array(metal_recycling) + np.array(paper_recycling)
plastic_percentage = (np.array(plastic_recycling) / total_recycling) * 100
glass_percentage = (np.array(glass_recycling) / total_recycling) * 100
metal_percentage = (np.array(metal_recycling) / total_recycling) * 100
paper_percentage = (np.array(paper_recycling) / total_recycling) * 100

ax[1].bar(months, plastic_percentage, color='#33FF57', alpha=0.8, label='Plastic')
ax[1].bar(months, glass_percentage, bottom=plastic_percentage, color='#FFD700', alpha=0.8, label='Glass')
ax[1].bar(months, metal_percentage, bottom=plastic_percentage + glass_percentage, color='#FF5733', alpha=0.8, label='Metal')
ax[1].bar(months, paper_percentage, bottom=plastic_percentage + glass_percentage + metal_percentage, color='#3357FF', alpha=0.8, label='Paper')

ax[1].set_xticks(x_indexes)
ax[1].set_xticklabels(months)
ax[1].set_title('Percentage Contribution to Total Recycling')
ax[1].legend()
ax[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()