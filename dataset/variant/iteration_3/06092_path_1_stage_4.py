import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Kids (5-12)', 'Teens (13-19)', 'Young Adults (20-30)', 'Adults (20-40)', 'Seniors (40+)']
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Non-fiction', 'Romance', 'Horror']

data = {
    'Kids (5-12)': [40, 10, 5, 20, 20, 5],
    'Teens (13-19)': [25, 30, 10, 15, 15, 5],
    'Young Adults (20-30)': [30, 25, 15, 20, 5, 5],
    'Adults (20-40)': [20, 15, 25, 30, 5, 5],
    'Seniors (40+)': [10, 10, 35, 30, 5, 10]
}

colors = ['#ff6f69', '#ffcc5c', '#88d8b0', '#c7f464', '#4da6ff', '#ffb7b2']

total_per_genre = np.array([sum(data[group][i] for group in age_groups) for i in range(len(genres))])

fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# Original mapping of subplots
mapping = [0, 1, 4, 3, 2]

for i, group_index in enumerate(mapping):
    group = age_groups[group_index]
    group_data = data[group]
    ax = axs[i // 3, i % 3]
    wedges, texts, autotexts = ax.pie(
        group_data,
        labels=genres,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        pctdistance=0.85,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=10)
    )
    
    ax.set(aspect="equal", title=f"{group}:\nFavorite Book Genres")
    ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

ax = axs[1, 2]
wedges, texts, autotexts = ax.pie(
    total_per_genre,
    labels=genres,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
    textprops=dict(size=10)
)

ax.set(aspect="equal", title="Overall: Favorite Book Genres Across All Age Groups")
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout(rect=[0, 0, 0.9, 0.95])
plt.suptitle('Book Genre Preferences Across Different Age Groups', fontsize=20, weight='bold')
plt.show()