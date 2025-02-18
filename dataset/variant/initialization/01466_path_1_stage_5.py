import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Blues']
market_share = [25, 18, 20, 15, 7, 5, 6, 4, 3, 2]
single_color = '#66b3ff'
explode = (0, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, colors=[single_color]*len(genres), autopct='%1.1f%%', startangle=90,
    explode=explode, shadow=False, wedgeprops={'edgecolor': 'gray'},
    pctdistance=0.8
)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("Market Share by Genre", fontsize=16)
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.grid(True)

plt.tight_layout()
plt.show()