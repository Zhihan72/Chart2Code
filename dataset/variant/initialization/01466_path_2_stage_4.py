import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Latin']
market_share = [23, 17, 18, 14, 6, 4, 5, 3, 3, 2]
single_color = '#66b3ff'  # Consistent color for all wedges
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, labels=genres, colors=[single_color] * len(genres), autopct='%1.1f%%', startangle=180,
    explode=explode, shadow=False, wedgeprops={'edgecolor': 'grey'}, textprops={'fontsize': 9}
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', lw=1.5, linestyle='--')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title(
    "Distribution of Popular Music Genres\nin Streaming Services (2023)",
    fontsize=13, fontweight='medium', pad=15
)

ax.legend(genres, title="Genres", loc="upper right", bbox_to_anchor=(0.9, 0.1), fontsize=9)

plt.grid(visible=True, linestyle=':')
plt.tight_layout()
plt.show()