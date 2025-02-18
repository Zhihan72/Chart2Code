import matplotlib.pyplot as plt

genres = ['RPG', 'Adventure', 'Action', 'Strategy', 'Shooter', 'Sports', 'Simulation']
market_shares = [20, 5, 25, 15, 12, 15, 8]
colors = ['#66b3ff', '#ff6666', '#ff9999', '#99ff99', '#c2c2f0', '#ffcc99', '#ffb3e6']
patterns = ['\\', 'o', '/', '|', 'x', '-', '+']
explode = (0.05, 0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, wedgeprops=dict(edgecolor='w', linewidth=1.5, alpha=0.9)
)

for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')
ax.set_title('Market Share by Genre', fontsize=14, pad=15)
ax.axis('equal')
plt.tight_layout()
plt.show()