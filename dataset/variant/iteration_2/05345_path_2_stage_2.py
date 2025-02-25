import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
lettuce_varieties = ['Romaine', 'Butterhead', 'Iceberg', 'Arugula']
sales_data = np.array([
    [10, 12, 14, 15, 18, 20, 22, 23, 21, 19, 15, 11],
    [8, 9, 10, 12, 14, 17, 19, 18, 16, 14, 10, 9],
    [9, 11, 13, 14, 16, 18, 20, 21, 20, 18, 13, 10],
    [5, 6, 8, 10, 12, 14, 16, 17, 15, 12, 8, 6]
])

single_color = '#4CAF50'  # Using a consistent green color

fig, axs = plt.subplots(2, 1, figsize=(12, 10), constrained_layout=True)

marker_styles = ['o', 's', 'D', '^']
line_styles = ['-', '--', '-.', ':']

# 1st subplot
for idx, variety in enumerate(lettuce_varieties):
    axs[0].plot(months, sales_data[idx], color=single_color, marker=marker_styles[idx], linestyle=line_styles[idx], alpha=0.7, label=variety)

axs[0].set_title('Monthly Lettuce Sales in 2023', fontsize=16, weight='bold')
axs[0].set_xlabel('Month', fontsize=12)
axs[0].set_ylabel('Sales (Thousands of Heads)', fontsize=12)
axs[0].legend(title='Lettuce Variety', loc='lower center', frameon=False)
axs[0].grid(True, which='major', color='gray', linestyle='-.', linewidth=0.75)

# 2nd subplot
bottom = np.zeros(len(months))
for idx, variety in enumerate(lettuce_varieties):
    axs[1].bar(months, sales_data[idx], bottom=bottom, color=single_color, alpha=0.7, label=variety)
    bottom += sales_data[idx]

axs[1].set_title('Portion of Lettuce Varieties Sold Each Month in 2023', fontsize=16, weight='bold')
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Sales (Thousands of Heads)', fontsize=12)
axs[1].legend(title='Lettuce Variety', loc='upper left', frameon=True, shadow=True)
axs[1].grid(True, which='minor', color='lightgray', linestyle=':', linewidth=0.5)

plt.show()