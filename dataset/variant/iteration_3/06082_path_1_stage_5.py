import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.arange(2015, 2024)
companies = ['TechCorp', 'CloudInc', 'DataSolutions', 'NetServices', 'AIInnovators']

storage_share = np.array([
    [40, 42, 45, 47, 50, 52, 55, 60, 62],
    [30, 28, 27, 25, 23, 20, 18, 17, 15],
    [20, 18, 17, 16, 15, 14, 13, 12, 11],
    [7, 8, 7, 8, 8, 9, 8, 6, 6],
    [3, 4, 4, 4, 4, 5, 6, 5, 6]
])

computing_share = np.array([
    [35, 37, 40, 41, 44, 45, 48, 50, 52],
    [30, 28, 26, 26, 25, 23, 21, 22, 20],
    [20, 18, 20, 19, 17, 17, 16, 16, 15],
    [10, 9, 8, 8, 8, 8, 8, 7, 7],
    [5, 8, 6, 6, 6, 7, 7, 5, 6]
])

ai_services_share = np.array([
    [45, 48, 50, 52, 55, 58, 60, 63, 65],
    [30, 25, 23, 21, 20, 18, 17, 16, 14],
    [10, 12, 12, 13, 13, 13, 13, 12, 11],
    [10, 8, 9, 8, 7, 6, 6, 6, 5],
    [5, 7, 6, 6, 5, 5, 4, 3, 5]
])

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 16), sharey=True)

# New set of colors
colors = ['#1f78b4', '#ff7f00', '#b2df8a', '#e31a1c', '#6a3d9a']

market_share_data = [storage_share, computing_share, ai_services_share]

for ax, data in zip(axes.flat[:3], market_share_data):  # Only use the first three axes, skipping the fourth
    bar_width = 0.15
    x_indexes = np.arange(len(years))
    
    for i in range(len(companies)):
        ax.bar(x_indexes + i * bar_width, data[i], width=bar_width, color=colors[i])
    
    ax.set_xticks(x_indexes + bar_width * 2)
    ax.set_xticklabels(years)
    ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_color('grey')
    ax.spines['left'].set_color('blue')
    ax.legend(companies, loc='upper left', fontsize='small', frameon=False)

plt.tight_layout()

plt.show()