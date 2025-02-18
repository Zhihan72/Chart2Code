import matplotlib.pyplot as plt

genres = ['RPG', 'Adventure', 'Strategy', 'Shooter', 'Action', 'Sports', 'Simulation']
market_shares = [20, 5, 15, 12, 25, 15, 8]
color = '#66b3ff'  # Single color applied consistently
explode = (0.05, 0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(6, 6))  # Plot initialized
wedges, texts, autotexts = ax.pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=160,
    colors=[color] * len(genres),  # Applying the single color to all wedges
    wedgeprops=dict(edgecolor='w', linewidth=1.5, alpha=0.9)
)

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')
ax.set_title('Genre Distribution', fontsize=13, pad=15)
ax.axis('equal')
plt.tight_layout()
plt.show()