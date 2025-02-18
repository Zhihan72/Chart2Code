import matplotlib.pyplot as plt

market_shares = [35, 25, 15, 10]
colors = ['#FFA07A', '#20B2AA', '#9370DB', '#FFD700']
explode = (0.1, 0, 0, 0)

plt.figure(figsize=(10, 7))
wedges, texts = plt.pie(
    market_shares, colors=colors, explode=explode, shadow=True,
    startangle=140
)

# Remove textual elements
for text in texts:
    text.set_visible(False)

plt.axis('equal')
plt.tight_layout()
plt.show()