import numpy as np
import matplotlib.pyplot as plt

# Create the data for the two remaining groups over 5 years
years = np.array([2017, 2018, 2019, 2020, 2021])
group_a_scores = np.array([76, 78, 82, 85, 87])
group_c_scores = np.array([70, 72, 74, 78, 80])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each group's scores
ax.plot(years, group_a_scores, label='Group A', marker='o', linestyle='-', linewidth=2, markersize=6, color='blue')
ax.plot(years, group_c_scores, label='Group C', marker='^', linestyle='-.', linewidth=2, markersize=6, color='red')

# Title and labels
ax.set_title('Annual Performance of Student Groups (2017-2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Score', fontsize=12)

# Customize the x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(60, 90, 5))

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='lower right', title='Groups')

# Annotate specific points
for i in range(len(years)):
    ax.annotate(f'{group_a_scores[i]}%', xy=(years[i], group_a_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
    ax.annotate(f'{group_c_scores[i]}%', xy=(years[i], group_c_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='red')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()