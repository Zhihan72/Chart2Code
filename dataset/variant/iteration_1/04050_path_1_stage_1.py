import numpy as np
import matplotlib.pyplot as plt

# Data for 3 groups over 5 years
years = np.array([2017, 2018, 2019, 2020, 2021])
group_a_scores = np.array([76, 78, 82, 85, 87])
group_b_scores = np.array([65, 68, 70, 75, 78])
group_c_scores = np.array([70, 72, 74, 78, 80])

# Figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot scores
ax.plot(years, group_a_scores, label='A', marker='o', linestyle='-', linewidth=2, markersize=6, color='blue')
ax.plot(years, group_b_scores, label='B', marker='s', linestyle='--', linewidth=2, markersize=6, color='green')
ax.plot(years, group_c_scores, label='C', marker='^', linestyle='-.', linewidth=2, markersize=6, color='red')

# Shortened title and labels
ax.set_title('Student Performance (2017-2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Avg Score', fontsize=12)

# Customize ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(60, 90, 5))

# Grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Legend with shortened title
ax.legend(loc='lower right', title='Grp')

# Annotate points
for i in range(len(years)):
    ax.annotate(f'{group_a_scores[i]}', xy=(years[i], group_a_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
    ax.annotate(f'{group_b_scores[i]}', xy=(years[i], group_b_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green')
    ax.annotate(f'{group_c_scores[i]}', xy=(years[i], group_c_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='red')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()