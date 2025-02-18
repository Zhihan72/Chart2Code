import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A recent study was conducted analyzing the happiness index across various age groups. 
# The study segmented participants into different age brackets and measured their happiness 
# levels using a standardized scale from 0 to 10 over a month.

# Age groups
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']

# Happiness scores for each age group (constructed data)
happiness_data = [
    [7, 8, 7, 6, 8, 8, 7, 9, 7, 6, 7, 8, 7, 8, 7],  # 18-25
    [6, 7, 6, 6, 7, 7, 6, 6, 6, 7, 6, 6, 5, 6, 6],  # 26-35
    [5, 6, 5, 6, 6, 5, 6, 6, 5, 5, 5, 5, 5, 6, 5],  # 36-45
    [6, 6, 5, 4, 5, 6, 5, 4, 4, 5, 6, 5, 4, 5, 5],  # 46-60
    [7, 6, 7, 6, 7, 7, 7, 6, 6, 7, 8, 7, 8, 7, 7]   # 60+
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Box plot configuration
box = ax.boxplot(happiness_data, vert=True, patch_artist=True, labels=age_groups, notch=True, meanline=True, showmeans=True)

# Customizing the appearance of the box plot
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#1E90FF', '#DA70D6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing means and medians
plt.setp(box['means'], color='blue')
plt.setp(box['medians'], color='red')

# Adding a line plot for median happiness scores
medians = [np.median(group) for group in happiness_data]
ax.plot(range(1, len(age_groups) + 1), medians, color='purple', marker='D', linestyle='-.', label='Median Happiness Score')

# Titles and labels
ax.set_title('Happiness Index Across Different Age Groups', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Happiness Score (0 to 10)', fontsize=12)
ax.set_xlabel('Age Groups', fontsize=12)

# Customize grid and background
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_facecolor('#f0f0f0')

# Add a legend
ax.legend()

# Annotate with additional information
for i, age_group in enumerate(age_groups):
    ax.text(i + 1, max(happiness_data[i]) + 0.5, f'Max: {max(happiness_data[i])}', 
            ha='center', fontsize=10, color=colors[i])

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()