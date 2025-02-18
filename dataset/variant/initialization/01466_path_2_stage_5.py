import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Latin']
market_share = [23, 17, 18, 14, 6, 4, 5, 3, 3, 2]
single_color = '#66b3ff'
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts = ax.pie(
    market_share, labels=None, colors=[single_color] * len(genres), autopct=None, startangle=180,
    explode=explode, shadow=False, wedgeprops={'edgecolor': 'grey'}
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', lw=1.5, linestyle='--')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.grid(visible=True, linestyle=':')
plt.tight_layout()
plt.show()