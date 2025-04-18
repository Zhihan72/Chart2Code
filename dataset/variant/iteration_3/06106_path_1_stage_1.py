import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-50)', 'Seniors (51+)']
fast_food_categories = ['Burgers', 'Pizza', 'Sandwiches', 'Tacos', 'Sushi', 'Salads']

data_by_age_group = {
    'Teens (13-19)': [30, 25, 10, 15, 10, 10],
    'Young Adults (20-35)': [20, 30, 20, 10, 10, 10],
    'Adults (36-50)': [15, 20, 20, 15, 15, 15],
    'Seniors (51+)': [10, 10, 25, 5, 10, 40]
}

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f1c40f', '#e74c3c']

# Create subplots in a 1x4 arrangement
fig, axs = plt.subplots(1, 4, figsize=(20, 5))

for i, (age_group, preferences) in enumerate(data_by_age_group.items()):
    ax = axs[i]
    
    wedges, texts, autotexts = ax.pie(
        preferences,
        labels=fast_food_categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=10)
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal", title=f"{age_group}\nFast Food Preferences")
    ax.legend(wedges, fast_food_categories, title="Food Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

fig.suptitle('Fast Food Preferences by Age Group in Flavortown', fontsize=16, y=1.01)

plt.tight_layout()
plt.show()