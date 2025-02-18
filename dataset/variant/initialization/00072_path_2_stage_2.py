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

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(12, 10))
wedges, texts, autotexts = ax.pie(
    overall_preference, 
    labels=genres, 
    colors=[single_color]*len(genres), 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w'), 
    autopct='%1.1f%%', 
    pctdistance=0.85
)

for genre in age_distribution.keys():
    ax.pie(
        age_distribution[genre], 
        radius=0.7, 
        colors=[single_color]*len(age_distribution[genre]), 
        startangle=140, 
        wedgeprops=dict(width=0.3, edgecolor='w')
    )

centre_circle = plt.Circle((0, 0), 0.35, fc='white')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

plt.title(
    "Literary Diet: Reading Preferences\nby Genre and Age",
    fontsize=14, 
    weight='bold'
)

plt.tight_layout()

plt.show()