import matplotlib.pyplot as plt

genres = ['Jazz', 'Country', 'Hip-Hop', 'Classical', 'Electronic', 'Pop', 'Reggae', 'Rock']
user_distribution = [15, 20, 3, 5, 12, 30, 7, 8]

explode = (0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1)
single_color = '#66b3ff'

plt.figure(figsize=(8, 6))
plt.pie(user_distribution, explode=explode, labels=genres, autopct='%1.1f%%',
        colors=[single_color]*len(genres), startangle=90, shadow=False,
        wedgeprops=dict(edgecolor='gray', width=0.4, linestyle='--'))

plt.title("Exploration of Melodic Preferences:\n2023 Music Analysis", fontsize=18, fontweight='regular')

plt.legend(genres, loc='upper right', title="Genres", title_fontsize='11', frameon=False)

plt.axis('equal')

plt.tight_layout()
plt.show()