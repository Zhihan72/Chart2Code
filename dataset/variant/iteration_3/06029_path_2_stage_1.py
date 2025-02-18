import matplotlib.pyplot as plt
import numpy as np

# Data: Monthly energy consumption (in GWh) for each colony over a year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
colony_alpha = [5.2, 5.5, 5.7, 5.6, 5.8, 5.9, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6]
colony_beta = [4.8, 4.9, 5.0, 5.1, 5.4, 5.6, 5.7, 5.8, 5.7, 5.6, 5.5, 5.3]
colony_gamma = [3.5, 3.6, 3.8, 3.9, 4.1, 4.2, 4.3, 4.4, 4.3, 4.2, 4.1, 3.9]

# Setup the figure and axes for subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [2, 1]})

# Histogram Plot for Monthly Energy Consumption
ax1 = axs[0]
data = list(colony_alpha + colony_beta + colony_gamma)
n, bins, patches = ax1.hist(data, bins=10, edgecolor='black', color='skyblue', alpha=0.7)
ax1.set_title('Energy Consumption in Mars Colonies (GWh)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Energy Consumption (GWh)', fontsize=14)
ax1.set_ylabel('Frequency', fontsize=14)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax1.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Stacked Bar Chart for Colony-wise Monthly Consumption
ax2 = axs[1]
width = 0.3
months_indices = np.arange(len(months))
uniform_color = '#66B3FF'  # A uniform blue color for all groups

ax2.bar(months_indices - width, colony_alpha, width, label='Colony Alpha', edgecolor='black', color=uniform_color, alpha=0.7)
ax2.bar(months_indices, colony_beta, width, label='Colony Beta', edgecolor='black', color=uniform_color, alpha=0.7)
ax2.bar(months_indices + width, colony_gamma, width, label='Colony Gamma', edgecolor='black', color=uniform_color, alpha=0.7)

ax2.set_title('Monthly Energy Consumption by Colony', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(months_indices)
ax2.set_xticklabels(months, fontsize=12)
ax2.set_ylabel('Energy Consumption (GWh)', fontsize=14)
ax2.legend(title='Colonies', loc='upper left', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()