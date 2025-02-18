import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart reflects the food preferences among populations of a fictional city, Flavortown. 
# Survey data reveals diverse choices in fast food categories consumed by different age groups.
# This helps local businesses to strategize their marketing for different age demographics.

# Data: Age Groups and Their Fast Food Preferences (in percentages)
age_groups = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-50)', 'Seniors (51+)']
fast_food_categories = ['Burgers', 'Pizza', 'Sandwiches', 'Tacos', 'Sushi', 'Salads']

# Data corresponding to age groups
data_by_age_group = {
    'Teens (13-19)': [30, 25, 10, 15, 10, 10],
    'Young Adults (20-35)': [20, 30, 20, 10, 10, 10],
    'Adults (36-50)': [15, 20, 20, 15, 15, 15],
    'Seniors (51+)': [10, 10, 25, 5, 10, 40]
}

# Colors for the pie chart slices
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f1c40f', '#e74c3c']

# Create subplots: each age group will have its own pie chart
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Loop through each age group to create a pie chart
for i, (age_group, preferences) in enumerate(data_by_age_group.items()):
    # Get the correct subplot axis
    ax = axs[i // 2][i % 2]
    
    # Create a pie chart for the given age group
    wedges, texts, autotexts = ax.pie(
        preferences,
        labels=fast_food_categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=10)
    )
    
    # Draw a white circle at the center to mimic a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    # Set the title for each subplot
    ax.set(aspect="equal", title=f"{age_group}\nFast Food Preferences")
    ax.legend(wedges, fast_food_categories, title="Food Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Overall title for the entire figure
fig.suptitle('Fast Food Preferences by Age Group in Flavortown', fontsize=16, y=1.01)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()