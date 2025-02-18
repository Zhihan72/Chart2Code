import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We want to visualize the average screen time usage for various types of applications on smartphones
# across different age groups in 2023. The applications monitored include social media, gaming, 
# productivity, and entertainment. 

# Data for age groups and screen time (in hours per day)
age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-39)', 'Middle-aged (40-49)', 'Seniors (50+)']
social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]
productivity = [1.2, 1.5, 1.8, 2.3, 1.9]
entertainment = [2.1, 2.4, 2.0, 1.5, 1.2]

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
width = 0.2  # Width of each bar 
y_pos = np.arange(len(age_groups))  # Positions for age groups

# Plot bars for each application category
bars1 = ax.barh(y_pos - 1.5*width, social_media, height=width, label='Social Media', color='royalblue')
bars2 = ax.barh(y_pos - 0.5*width, gaming, height=width, label='Gaming', color='tomato')
bars3 = ax.barh(y_pos + 0.5*width, productivity, height=width, label='Productivity', color='forestgreen')
bars4 = ax.barh(y_pos + 1.5*width, entertainment, height=width, label='Entertainment', color='gold')

# Adding titles and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(age_groups, fontsize=12)
ax.set_xlabel('Average Screen Time (Hours per Day)', fontsize=12)
ax.set_title('Average Smartphone Screen Time by Application Type and Age Group in 2023', fontsize=16, fontweight='bold')

# Adding grid lines for x-axis
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adding a legend
ax.legend(title='Application Type', fontsize=10, loc='best')

# Function to annotate screen time values on each bar
def add_values(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', va='center', fontsize=10)

add_values(bars1)
add_values(bars2)
add_values(bars3)
add_values(bars4)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()