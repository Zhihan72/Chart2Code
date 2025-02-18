import matplotlib.pyplot as plt

# Expanded list of genres with a new entry
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance', 'Fantasy']
overall_preference = [35, 25, 20, 10, 10, 15]

# Expanded age distribution to include 'Fantasy'
age_groups = ['Kids', 'Teens', 'Adults', 'Seniors']
age_distribution = {
    'Fiction': [25, 20, 45, 10],
    'Non-Fiction': [10, 15, 50, 25],
    'Mystery': [5, 15, 55, 25],
    'Science Fiction': [15, 25, 45, 15],
    'Romance': [10, 15, 50, 25],
    'Fantasy': [20, 30, 30, 20]
}

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=[single_color]*len(genres),
                                  startangle=60, wedgeprops=dict(width=0.3, edgecolor='w'),
                                  autopct='%1.1f%%', pctdistance=0.8)

for i, genre in enumerate(genres):
    ax.pie(age_distribution[genre], radius=0.7, colors=[single_color]*len(age_distribution[genre]),
           startangle=60, wedgeprops=dict(width=0.3, edgecolor='b'))

centre_circle = plt.Circle((0,0),0.35,fc='white')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

ax.legend(wedges, age_groups, title="Age Groups", loc="upper right", bbox_to_anchor=(1.1, 0.9))
ax.spines['bottom'].set_linestyle('dotted')

plt.title("Literary Preferences \nGenre and Age Analysis", fontsize=16, weight='bold')

ax.xaxis.grid(True, linestyle='dashed')
ax.yaxis.grid(True, linestyle='dashed')

plt.tight_layout()
plt.show()