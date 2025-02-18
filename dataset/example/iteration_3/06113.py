import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the technology stacks being evaluated
categories = ['Frontend', 'Backend', 'Database', 'DevOps', 'AI/ML', 'Security']
num_vars = len(categories)

# Proficiency levels (out of 10) in various technology stacks for each team
frontend_gurus = [9, 6, 3, 5, 4, 5]
backend_masters = [5, 9, 8, 6, 3, 4]
database_whizzes = [4, 7, 9, 5, 6, 5]
devops_ninjas = [6, 5, 4, 9, 3, 8]

# Create a 2D array for the proficiency levels of all teams
proficiency_data = [frontend_gurus, backend_masters, database_whizzes, devops_ninjas]

# Names of teams
teams = ["Frontend Gurus", "Backend Masters", "Database Whizzes", "DevOps Ninjas"]

# Compute angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop by adding the first angle at the end

# Function to create a radar chart
def create_radar_chart(ax, data, labels, colors):
    for i, (team_data, team_name, color) in enumerate(zip(data, teams, colors)):
        team_data += team_data[:1]
        ax.plot(angles, team_data, linewidth=2, linestyle='solid', label=team_name, color=color)
        ax.fill(angles, team_data, alpha=0.2, color=color)
    
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels([str(x) for x in range(0, 11, 2)], fontsize=8)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define colors for each team
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create radar chart with given data
create_radar_chart(ax, proficiency_data, categories, colors)

# Add a title and legend
plt.title("Tech Stack Proficiency Comparison Among IT Teams", fontsize=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)

# Optimize layout to prevent overlap
plt.tight_layout()
plt.show()