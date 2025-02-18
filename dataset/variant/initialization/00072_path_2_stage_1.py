import matplotlib.pyplot as plt

# Data Preparation
genres = ['Fiction', 'Non-F', 'Mystery', 'Sci-Fi', 'Romance', 'Thriller', 'Fantasy']
overall_preference = [20, 15, 15, 10, 10, 15, 15]

age_groups = ['Kids', 'Teens', 'YA', 'Adults', 'Seniors']
age_distribution = {
    'Fiction': [10, 20, 30, 30, 10],
    'Non-Fiction': [5, 15, 20, 35, 25],
    'Mystery': [3, 12, 25, 40, 20],
    'Science Fiction': [12, 18, 25, 30, 15],
    'Romance': [5, 15, 25, 35, 20],
    'Thriller': [10, 20, 30, 30, 10],
    'Fantasy': [20, 15, 25, 25, 15],
}

genre_colors = ['#8B008B', '#FF8C00', '#4682B4', '#32CD32', '#FF1493', '#B22222', '#20B2AA']
age_colors = ['#F4A460', '#00FA9A', '#6495ED', '#FFD700', '#D2691E']

fig, ax = plt.subplots(figsize=(12, 10))
wedges, texts, autotexts = ax.pie(
    overall_preference, 
    labels=genres, 
    colors=genre_colors, 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w'), 
    autopct='%1.1f%%', 
    pctdistance=0.85
)

# Draw the outer rings for age distribution
for i, genre in enumerate(age_distribution.keys()):
    ax.pie(
        age_distribution[genre], 
        radius=0.7, 
        colors=age_colors, 
        startangle=140, 
        wedgeprops=dict(width=0.3, edgecolor='w')
    )

# Center circle for donut shape
centre_circle = plt.Circle((0, 0), 0.35, fc='white')
fig.gca().add_artist(centre_circle)

# Customize text colors
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Informative legend
ax.legend(wedges, age_groups, title="Age Grps", loc="center left", bbox_to_anchor=(1, 0.5))

# Shortened title
plt.title(
    "Literary Diet: Reading Preferences\nby Genre and Age",
    fontsize=14, 
    weight='bold'
)

plt.tight_layout()

plt.show()