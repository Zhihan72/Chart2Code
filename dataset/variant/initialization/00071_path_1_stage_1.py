import matplotlib.pyplot as plt

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance']
overall_preference = [35, 25, 20, 10, 10]
age_groups = ['Kids', 'Teens', 'Adults', 'Seniors']
age_distribution = {
    'Fiction': [25, 20, 45, 10],
    'Non-Fiction': [10, 15, 50, 25],
    'Mystery': [5, 15, 55, 25],
    'Science Fiction': [15, 25, 45, 15],
    'Romance': [10, 15, 50, 25],
}

# New set of colors and marker styles
genre_colors = ['#FF6347', '#4682B4', '#6A5ACD', '#9ACD32', '#FF4500']
age_colors = ['#CD5C5C', '#20B2AA', '#9370DB', '#FFDAB9']
line_styles = ['dashed', 'dotted', 'dashdot']
marker_shapes = ['o', 's', 'D', '*']

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=genre_colors, 
                                  startangle=60, wedgeprops=dict(width=0.3, edgecolor='w'),
                                  autopct='%1.1f%%', pctdistance=0.8)

# Outer ring for age distribution with different style
for i, genre in enumerate(genres):
    ax.pie(age_distribution[genre], radius=0.7, colors=age_colors,
           startangle=60, wedgeprops=dict(width=0.3, edgecolor='b'))

# Central circle for donut plot
centre_circle = plt.Circle((0,0),0.35,fc='white')
fig.gca().add_artist(centre_circle)

# Text properties update
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Different legend position and line style
ax.legend(wedges, age_groups, title="Age Groups", loc="upper right", bbox_to_anchor=(1.1, 0.9))
ax.spines['bottom'].set_linestyle('dotted')

# Title with line changed
plt.title("Literary Preferences \nGenre and Age Analysis", fontsize=16, weight='bold')

# Show grid with a custom style
ax.xaxis.grid(True, linestyle='dashed')
ax.yaxis.grid(True, linestyle='dashed')

plt.tight_layout()
plt.show()