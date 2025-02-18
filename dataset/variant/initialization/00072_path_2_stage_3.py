import matplotlib.pyplot as plt

genres = ['Fiction', 'Non-F', 'Mystery', 'Sci-Fi', 'Romance', 'Thriller', 'Fantasy']
overall_preference = [20, 15, 15, 10, 10, 15, 15]

age_distribution = {
    'Fiction': [10, 20, 30, 30, 10],
    'Non-Fiction': [5, 15, 20, 35, 25],
    'Mystery': [3, 12, 25, 40, 20],
    'Science Fiction': [12, 18, 25, 30, 15],
    'Romance': [5, 15, 25, 35, 20],
    'Thriller': [10, 20, 30, 30, 10],
    'Fantasy': [20, 15, 25, 25, 15],
}

colors = ['#6495ED', '#FF6347', '#FFD700', '#ADFF2F', '#FF69B4', '#8A2BE2', '#7FFFD4']
linestyle_choices = ['-', '--', '-.', ':']
marker_choices = ['o', '^', 's', 'D', 'X', '*']

fig, ax = plt.subplots(figsize=(12, 10))
wedges, texts, autotexts = ax.pie(
    overall_preference, 
    labels=genres, 
    colors=colors, 
    startangle=100, 
    wedgeprops=dict(width=0.4, edgecolor='k'), 
    autopct='%1.1f%%', 
    pctdistance=0.8
)

for i, genre in enumerate(age_distribution.keys()):
    marker_style = marker_choices[i % len(marker_choices)]
    linestyle = linestyle_choices[i % len(linestyle_choices)]
    ax.pie(
        age_distribution[genre], 
        radius=0.7+0.03*i, 
        colors=colors, 
        startangle=100, 
        wedgeprops=dict(width=0.35, edgecolor='k', linestyle=linestyle)
    )

centre_circle = plt.Circle((0, 0), 0.36, fc='lightgray')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

plt.title(
    "Literary Diet: Reading Preferences\nby Genre and Age",
    fontsize=16, 
    weight='bold'
)

ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.grid(True)

plt.show()