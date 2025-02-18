import matplotlib.pyplot as plt

# Altered labels for randomness
genres = ['RPG', 'Adventure', 'Strategy', 'Shooter', 'Action', 'Sports', 'Simulation']
market_shares = [20, 5, 15, 12, 25, 15, 8]
colors = ['#66b3ff', '#ff6666', '#ff9999', '#99ff99', '#c2c2f0', '#ffcc99', '#ffb3e6']
patterns = ['x', 'o', '/', '\\', '|', '-', '+']
explode = (0.05, 0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=160,
    colors=colors, wedgeprops=dict(edgecolor='w', linewidth=1.5, alpha=0.9)
)

for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')
ax.set_title('Genre Distribution', fontsize=13, pad=15)  # Title changed
ax.axis('equal')
plt.tight_layout()
plt.show()