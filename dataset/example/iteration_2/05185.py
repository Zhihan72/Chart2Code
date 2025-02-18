import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are visualizing a fictional study on the hobby preferences among different age groups.
# The study aims to understand how various hobbies are distributed among age ranges from teenagers to senior citizens.

# Define Age Groups and Hobbies
age_groups = ['Teenagers', 'Young Adults', 'Adults', 'Middle-aged', 'Seniors']
hobbies = ['Reading', 'Gaming', 'Traveling', 'Painting', 'Gardening']

# Data representing the percentage of each age group involved in each hobby
data = np.array([
    [30, 50, 20, 10, 5],   # Teenagers
    [40, 60, 25, 15, 10],  # Young Adults
    [50, 40, 30, 20, 15],  # Adults
    [45, 30, 40, 25, 20],  # Middle-aged
    [35, 25, 40, 30, 40]   # Seniors
])

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 9))

# Bar chart for hobby distribution among age groups
bar_width = 0.15
indices = np.arange(len(hobbies))

# Define colors for age groups
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Stacked bar chart
for i in range(len(age_groups)):
    axes[0].bar(indices + i * bar_width, data[i], bar_width, label=age_groups[i], color=colors[i])

axes[0].set_title('Hobby Preferences Among Different Age Groups', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Hobbies', fontsize=13)
axes[0].set_ylabel('Percentage of People Involved', fontsize=13)
axes[0].set_xticks(indices + bar_width * (len(age_groups) / 2 - 0.5))
axes[0].set_xticklabels(hobbies, fontsize=12)
axes[0].legend(title='Age Groups', fontsize=11)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Create a pie chart for overall hobby preferences
total_hobby_counts = data.sum(axis=0)
colors_pie = plt.cm.viridis(np.arange(5)/5.)
axes[1].pie(total_hobby_counts, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=colors_pie,
            wedgeprops=dict(edgecolor='black'), textprops=dict(color="white"))

axes[1].set_title('Overall Hobby Preferences', fontsize=16, fontweight='bold')

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()