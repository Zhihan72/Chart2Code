import matplotlib.pyplot as plt

genres = ['Jazz', 'Country', 'Hip-Hop', 'Classical', 'Electronic', 'Pop', 'Reggae', 'Rock']
user_distribution = [15, 20, 3, 5, 12, 30, 7, 8]

colors = ['#ff9999', '#66b3ff', '#ff6666', '#e6e600', '#ffcc99', '#99ff99', '#ffb3e6', '#c2c2f0']
explode = (0, 0, 0, 0, 0, 0.1, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, labels=genres, autopct='%1.1f%%',
        colors=colors, startangle=140, shadow=True, wedgeprops=dict(edgecolor='w', width=0.3))

plt.title("Exploration of Melodic Preferences:\n2023 Music Analysis", fontsize=16, fontweight='bold', pad=20)

plt.legend(genres, loc='center left', bbox_to_anchor=(1, 0.5), title="Trend Categories", title_fontsize='13')

plt.axis('equal')
plt.tight_layout()
plt.show()