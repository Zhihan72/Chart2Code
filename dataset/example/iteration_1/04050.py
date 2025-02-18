import numpy as np
import matplotlib.pyplot as plt

# Title and Backstory:
# The chart is about tracking the performance of three student groups across different years in a particular subject. 
# We're interested in seeing how their average scores have progressed over time.

# Create the data for the three groups over 5 years
years = np.array([2017, 2018, 2019, 2020, 2021])
group_a_scores = np.array([76, 78, 82, 85, 87])
group_b_scores = np.array([65, 68, 70, 75, 78])
group_c_scores = np.array([70, 72, 74, 78, 80])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each group's scores
ax.plot(years, group_a_scores, label='Group A', marker='o', linestyle='-', linewidth=2, markersize=6, color='blue')
ax.plot(years, group_b_scores, label='Group B', marker='s', linestyle='--', linewidth=2, markersize=6, color='green')
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
    ax.annotate(f'{group_b_scores[i]}%', xy=(years[i], group_b_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green')
    ax.annotate(f'{group_c_scores[i]}%', xy=(years[i], group_c_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='red')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()