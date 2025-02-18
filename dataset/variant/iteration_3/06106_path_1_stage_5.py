import matplotlib.pyplot as plt

age_groups = ['Teens', 'Y Adults', 'Adults', 'Seniors', 'Middle-aged']
fast_food_categories = ['Burgers', 'Pizza', 'Sandwiches', 'Tacos', 'Sushi', 'Salads']

data_by_age_group = {
    'Teens': [30, 25, 10, 15, 10, 10],
    'Y Adults': [20, 30, 20, 10, 10, 10],
    'Adults': [15, 20, 20, 15, 15, 15],
    'Seniors': [10, 10, 25, 5, 10, 40],
    'Middle-aged': [20, 15, 25, 10, 5, 25]
}

colors_shuffled = [
    ['#66b3ff', '#ff9999', '#e74c3c', '#f1c40f', '#99ff99', '#ffcc99'],
    ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#e74c3c', '#f1c40f'],
    ['#ff9999', '#f1c40f', '#ffcc99', '#66b3ff', '#99ff99', '#e74c3c'],
    ['#99ff99', '#e74c3c', '#66b3ff', '#ff9999', '#ffcc99', '#f1c40f'],
    ['#e74c3c', '#ff9999', '#99ff99', '#66b3ff', '#f1c40f', '#ffcc99']
]

fig, axs = plt.subplots(1, 5, figsize=(25, 5))

for i, (age_group, preferences) in enumerate(data_by_age_group.items()):
    ax = axs[i]
    
    wedges, texts, autotexts = ax.pie(
        preferences,
        labels=fast_food_categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors_shuffled[i],
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=10)
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    ax.set(aspect="equal", title=f"{age_group} Preferences")
    ax.legend(wedges, fast_food_categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

fig.suptitle('Preferences by Age Group in Flavortown', fontsize=16, y=1.01)

plt.tight_layout()
plt.show()