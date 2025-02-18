import matplotlib.pyplot as plt

# Data for plotting
age_groups = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-50)', 'Seniors (51+)']
fast_food_categories = ['Burgers', 'Pizza', 'Sandwiches', 'Tacos', 'Sushi', 'Salads']
data_by_age_group = {
    'Teens (13-19)': [30, 25, 10, 15, 10, 10],
    'Young Adults (20-35)': [20, 30, 20, 10, 10, 10],
    'Adults (36-50)': [15, 20, 20, 15, 15, 15],
    'Seniors (51+)': [10, 10, 25, 5, 10, 40]
}
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f1c40f', '#e74c3c']

# Create subplots without textual elements
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

for i, (age_group, preferences) in enumerate(data_by_age_group.items()):
    ax = axs[i // 2][i % 2]
    wedges, _ = ax.pie(
        preferences,
        labels=['']*len(fast_food_categories),  # Remove the labels
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5)
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()