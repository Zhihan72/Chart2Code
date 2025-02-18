import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# The chart visualizes the favorite fruits among children and adults in a community, 
# aiming to showcase the preference similarities and differences.

# Fruits categories
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']

# Data: percentage of each fruit preference among children and adults
children_preferences = [30, 20, 15, 25, 10]
adults_preferences = [25, 15, 30, 20, 10]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width
bar_width = 0.4

# Define positions of the bars
indices = np.arange(len(fruits))
children_index = indices - bar_width/2
adults_index = indices + bar_width/2

# Plotting bars for children and adults
bars_children = ax.bar(children_index, children_preferences, width=bar_width, label='Children', color='#FFA07A')
bars_adults = ax.bar(adults_index, adults_preferences, width=bar_width, label='Adults', color='#20B2AA')

# Adding title and labels
ax.set_title("Fruit Preferences among Children and Adults in the Community", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Fruits", fontsize=14)
ax.set_ylabel("Preferences (%)", fontsize=14)

# Customize ticks on the x-axis
ax.set_xticks(indices)
ax.set_xticklabels(fruits, fontsize=12)

# Adding percentages above the bars for clear visibility
for bars in (bars_children, bars_adults):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

# Adding a legend
ax.legend(title='Age Group')

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to include titles and labels
plt.tight_layout()

# Show plot
plt.show()