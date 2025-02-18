import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Kids (5-12)', 'Teens (13-19)', 'Adults (20-40)', 'Seniors (40+)']
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Non-fiction', 'Romance', 'Horror']

data = {
    'Kids (5-12)': [40, 10, 5, 20, 20, 5],
    'Teens (13-19)': [25, 30, 10, 15, 15, 5],
    'Adults (20-40)': [20, 15, 25, 30, 5, 5],
    'Seniors (40+)': [10, 10, 35, 30, 5, 10]
}

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

total_per_genre = np.array([sum(data[group][i] for group in age_groups) for i in range(len(genres))])

fig, axs = plt.subplots(3, 2, figsize=(12, 18))

for i, (group, group_data) in enumerate(data.items()):
    ax = axs[i // 2, i % 2]
    wedges, _ = ax.pie(
        group_data,
        colors=colors,
        startangle=90,
        pctdistance=0.85,
        wedgeprops=dict(edgecolor='w', linewidth=0.5),
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal")

ax = axs[2, 0]
wedges, _ = ax.pie(
    total_per_genre,
    colors=colors,
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w', linewidth=0.5),
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.set(aspect="equal")

plt.tight_layout(rect=[0, 0, 0.9, 0.95])

plt.show()