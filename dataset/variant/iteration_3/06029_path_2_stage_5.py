import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
colony_alpha = [5.2, 5.5, 5.7, 5.6, 5.8, 5.9, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6]
colony_beta = [4.8, 4.9, 5.0, 5.1, 5.4, 5.6, 5.7, 5.8, 5.7, 5.6, 5.5, 5.3]
colony_gamma = [3.5, 3.6, 3.8, 3.9, 4.1, 4.2, 4.3, 4.4, 4.3, 4.2, 4.1, 3.9]
colony_delta = [4.1, 4.3, 4.5, 4.4, 4.6, 4.8, 4.9, 5.0, 4.9, 4.7, 4.6, 4.4]
colony_epsilon = [3.8, 3.9, 4.0, 4.1, 4.3, 4.4, 4.5, 4.6, 4.5, 4.3, 4.2, 4.0]

fig, axs = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [2, 1]})

ax1 = axs[0]
width = 0.15
months_indices = np.arange(len(months))
colors = ['#66B3FF', '#FFB366', '#66FFB3', '#FF66B3', '#B366FF']

ax1.bar(months_indices - 2*width, colony_alpha, width, edgecolor='black', color=colors[0], alpha=0.7, label='Colony Alpha')
ax1.bar(months_indices - width, colony_beta, width, edgecolor='black', color=colors[1], alpha=0.7, label='Colony Beta')
ax1.bar(months_indices, colony_gamma, width, edgecolor='black', color=colors[2], alpha=0.7, label='Colony Gamma')
ax1.bar(months_indices + width, colony_delta, width, edgecolor='black', color=colors[3], alpha=0.7, label='Colony Delta')
ax1.bar(months_indices + 2*width, colony_epsilon, width, edgecolor='black', color=colors[4], alpha=0.7, label='Colony Epsilon')

ax1.set_title('Monthly Energy Consumption by Colony', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(months_indices)
ax1.set_xticklabels(months, fontsize=12)
ax1.set_ylabel('Energy Consumption (GWh)', fontsize=14)
ax1.legend()

# Remove borders
for spine in ax1.spines.values():
    spine.set_visible(False)

ax2 = axs[1]
data = list(colony_alpha + colony_beta + colony_gamma + colony_delta + colony_epsilon)
n, bins, patches = ax2.hist(data, bins=10, edgecolor='black', color='skyblue', alpha=0.7)
ax2.set_title('Energy Consumption in Mars Colonies (GWh)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Energy Consumption (GWh)', fontsize=14)
ax2.set_ylabel('Frequency', fontsize=14)

# Remove borders
for spine in ax2.spines.values():
    spine.set_visible(False)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax2.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()