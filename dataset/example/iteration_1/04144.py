import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Imagine we are exploring the productivity of different teams in a tech company over a period of 6 months.
# This chart shows the number of features each team has completed monthly in the first half of the year.

# Data: Monthly features completed by three different teams
months = np.array([1, 2, 3, 4, 5, 6])
team_alpha = np.array([5, 10, 15, 20, 25, 30])
team_beta = np.array([7, 14, 21, 28, 35, 42])
team_gamma = np.array([4, 9, 12, 18, 24, 29])

# Create a figure and plot the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each team's feature completion count with different styles
ax.plot(months, team_alpha, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Team Alpha')
ax.plot(months, team_beta, marker='s', linestyle='--', color='#33FFBD', linewidth=2, label='Team Beta')
ax.plot(months, team_gamma, marker='^', linestyle='-.', color='#335BFF', linewidth=2, label='Team Gamma')

# Annotate specific data points
for (month, alpha_feat, beta_feat, gamma_feat) in zip(months, team_alpha, team_beta, team_gamma):
    ax.annotate(f'{alpha_feat}', (month, alpha_feat), textcoords="offset points", xytext=(-10,10), ha='center')
    ax.annotate(f'{beta_feat}', (month, beta_feat), textcoords="offset points", xytext=(10,-15), ha='center')
    ax.annotate(f'{gamma_feat}', (month, gamma_feat), textcoords="offset points", xytext=(-10,-20), ha='center')

# Adding grid lines for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Set x and y labels, title and legend
ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Features Completed', fontsize=12, fontweight='bold')
ax.set_title('Feature Completion Trend of Different Teams (Jan-Jun)\nProductivity Monitoring in a Tech Company', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
ax.legend(loc='upper left', title='Teams')

# Automatically adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()