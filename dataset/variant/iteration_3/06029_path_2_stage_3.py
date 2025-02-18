import matplotlib.pyplot as plt
import numpy as np

# Data with additional colonies
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
colony_alpha = [5.2, 5.5, 5.7, 5.6, 5.8, 5.9, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6]
colony_beta = [4.8, 4.9, 5.0, 5.1, 5.4, 5.6, 5.7, 5.8, 5.7, 5.6, 5.5, 5.3]
colony_gamma = [3.5, 3.6, 3.8, 3.9, 4.1, 4.2, 4.3, 4.4, 4.3, 4.2, 4.1, 3.9]
colony_delta = [4.1, 4.3, 4.5, 4.4, 4.6, 4.8, 4.9, 5.0, 4.9, 4.7, 4.6, 4.4]
colony_epsilon = [3.8, 3.9, 4.0, 4.1, 4.3, 4.4, 4.5, 4.6, 4.5, 4.3, 4.2, 4.0]

# Setup the figure
fig, axs = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [2, 1]})

# Stacked Bar Chart with additional data
ax1 = axs[0]
width = 0.18
months_indices = np.arange(len(months))
colors = ['#66B3FF', '#FFB366', '#66FFB3', '#FF66B3', '#B366FF']

ax1.bar(months_indices - 2*width, colony_alpha, width, label='Colony Alpha', edgecolor='black', color=colors[0], alpha=0.7)
ax1.bar(months_indices - width, colony_beta, width, label='Colony Beta', edgecolor='black', color=colors[1], alpha=0.7)
ax1.bar(months_indices, colony_gamma, width, label='Colony Gamma', edgecolor='black', color=colors[2], alpha=0.7)
ax1.bar(months_indices + width, colony_delta, width, label='Colony Delta', edgecolor='black', color=colors[3], alpha=0.7)
ax1.bar(months_indices + 2*width, colony_epsilon, width, label='Colony Epsilon', edgecolor='black', color=colors[4], alpha=0.7)

ax1.set_title('Monthly Energy Consumption by Colony', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(months_indices)
ax1.set_xticklabels(months, fontsize=12)
ax1.set_ylabel('Energy Consumption (GWh)', fontsize=14)
ax1.legend(title='Colonies', loc='upper left', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

# Histogram Plot for Monthly Energy Consumption
ax2 = axs[1]
data = list(colony_alpha + colony_beta + colony_gamma + colony_delta + colony_epsilon)
n, bins, patches = ax2.hist(data, bins=10, edgecolor='black', color='skyblue', alpha=0.7)
ax2.set_title('Energy Consumption in Mars Colonies (GWh)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Energy Consumption (GWh)', fontsize=14)
ax2.set_ylabel('Frequency', fontsize=14)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax2.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()