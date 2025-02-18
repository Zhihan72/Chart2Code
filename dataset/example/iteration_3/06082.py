import matplotlib.pyplot as plt
import numpy as np

# Backstory: Different tech companies are vying for market share in various cloud services. 
# This chart visualizes the market share trends of these companies in storage, computing, and AI services from 2015 to 2023.

# Define the years and companies
years = np.arange(2015, 2024)
companies = ['TechCorp', 'CloudInc', 'DataSolutions', 'NetServices', 'AIInnovators']

# Market share data for cloud services (values in percentages)
storage_share = np.array([
    [40, 42, 45, 47, 50, 52, 55, 60, 62],  # TechCorp
    [30, 28, 27, 25, 23, 20, 18, 17, 15],   # CloudInc
    [20, 18, 17, 16, 15, 14, 13, 12, 11],   # DataSolutions
    [7, 8, 7, 8, 8, 9, 8, 6, 6],           # NetServices
    [3, 4, 4, 4, 4, 5, 6, 5, 6]            # AIInnovators
])

computing_share = np.array([
    [35, 37, 40, 41, 44, 45, 48, 50, 52],  # TechCorp
    [30, 28, 26, 26, 25, 23, 21, 22, 20],  # CloudInc
    [20, 18, 20, 19, 17, 17, 16, 16, 15],  # DataSolutions
    [10, 9, 8, 8, 8, 8, 8, 7, 7],          # NetServices
    [5, 8, 6, 6, 6, 7, 7, 5, 6]           # AIInnovators
])

ai_services_share = np.array([
    [45, 48, 50, 52, 55, 58, 60, 63, 65],  # TechCorp
    [30, 25, 23, 21, 20, 18, 17, 16, 14],  # CloudInc
    [10, 12, 12, 13, 13, 13, 13, 12, 11],  # DataSolutions
    [10, 8, 9, 8, 7, 6, 6, 6, 5],          # NetServices
    [5, 7, 6, 6, 5, 5, 4, 3, 5]           # AIInnovators
])

# Create the figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 8), sharey=True)

# Colors for the companies
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Titles for the subplots
titles = ['Storage Services Market Share', 'Computing Services Market Share', 'AI Services Market Share']

# Market share data arrays for ease of iteration
market_share_data = [storage_share, computing_share, ai_services_share]

# Plot stacked bars for each type of service and company
for ax, data, title in zip(axes, market_share_data, titles):
    bar_width = 0.15
    x_indexes = np.arange(len(years))
    
    for i, company in enumerate(companies):
        ax.bar(x_indexes + i * bar_width, data[i], width=bar_width, label=company if title == titles[0] else "", color=colors[i])
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x_indexes + bar_width * 2)
    ax.set_xticklabels(years)
    ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

axes[0].set_ylabel('Market Share (%)', fontsize=12)

# Combine unique handles and labels for a single legend
handles, labels = axes[0].get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
fig.legend(unique_labels.values(), unique_labels.keys(), loc='upper center', fontsize=10, ncol=3, title='Company')

# Automatically adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()