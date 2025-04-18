import matplotlib.pyplot as plt

genres = ['Action', 'RPG', 'Sports', 'Strategy']
market_shares = [35, 25, 15, 10]

colors = ['#FFA07A', '#20B2AA', '#9370DB', '#FFD700']
explode = (0.1, 0, 0, 0)

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
plt.tight_layout()
plt.show()