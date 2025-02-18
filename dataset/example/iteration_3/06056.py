import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Sleep Patterns Across Different Age Groups
# The goal is to investigate the distribution of sleep duration (in hours) across various age groups.

# Defining the artificial data
children = [9, 9, 10, 11, 10, 9, 10, 11, 12, 9, 10, 11, 8, 9, 10, 11, 10, 9, 10]
teenagers = [7, 8, 9, 7, 8, 7, 8, 9, 7, 8, 9, 7, 8, 9, 8, 8, 7, 9]
young_adults = [6, 6, 7, 6, 7, 6, 6, 7, 7, 6, 7, 6, 6, 7]
adults = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 6, 5, 6, 5]
seniors = [6, 6, 7, 6, 6, 7, 6, 7, 6, 6, 7, 6, 7, 6, 6]

# Combining all groups for violin plot
data = [children, teenagers, young_adults, adults, seniors]
age_groups = ['Children (6-12)', 'Teenagers (13-19)', 'Young Adults (20-35)', 'Adults (36-55)', 'Seniors (56+)']

# Create the figure and subplots
fig, ax = plt.subplots(figsize=(10, 7))

# Create the violin plot
violin = ax.violinplot(data, showmeans=False, showmedians=True)

# Customize the violin plot
colors = ['#add8e6', '#ffcccb', '#c3e6cb', '#fdd835', '#9575cd']
for patch, color in zip(violin['bodies'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_alpha(0.7)

# Title and labels
plt.title('Analysis of Sleep Patterns Across Different Age Groups', fontsize=16, fontweight='bold')
plt.ylabel('Age Groups', fontsize=12)
plt.xlabel('Sleep Duration (hours)', fontsize=12)
plt.yticks(range(1, len(age_groups) + 1), age_groups, fontsize=10)

# Annotate with mean values for additional context
for i, group in enumerate(data):
    mean_val = np.mean(group)
    plt.text(mean_val + 0.1, i + 1, f'Mean: {mean_val:.1f}h', verticalalignment='center', fontsize=9, color='darkblue')

# Add a legend for the median
ax.scatter([], [], color='red', label='Median')  # Dummy point for legend
plt.legend(loc='upper right', fontsize=10)

# Grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()