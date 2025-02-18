import matplotlib.pyplot as plt

genres = ['Act', 'RPG', 'Sprt', 'Strat', 'Sim', 'Puzz']
market_shares = [15, 35, 7, 25, 10, 8]
colors = ['#33FFFF', '#FF5733', '#FFD700', '#3357FF', '#FF33FF', '#33FF57']  # Shuffled colors
explode = (0, 0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    market_shares, labels=genres, colors=colors, explode=explode, shadow=True,
    autopct='%1.1f%%', startangle=140
)

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.title('Game Genre Market Share 2023', fontsize=16, fontweight='bold')

plt.legend(wedges, genres, title="Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)
plt.tight_layout()
plt.show()