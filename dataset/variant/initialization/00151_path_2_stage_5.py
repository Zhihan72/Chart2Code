import matplotlib.pyplot as plt

genres = ['RPG', 'Adventure', 'Strategy', 'Shooter', 'Action', 'Sports', 'Simulation']
market_shares = [20, 5, 15, 12, 25, 15, 8]
color = '#66b3ff'
explode = (0.05, 0, 0, 0, 0.1, 0, 0)

# Modifying the subplot arrangement to have different rows and columns
fig, axarr = plt.subplots(2, 1, figsize=(8, 8))  # Changed to 2 rows and 1 column

# Use the first subplot axis to draw the pie chart
wedges, texts, autotexts = axarr[0].pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=160,
    colors=[color] * len(genres),
    wedgeprops=dict(edgecolor='w', linewidth=1.5, alpha=0.9)
)

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')
axarr[0].set_title('Genre Distribution', fontsize=13, pad=15)
axarr[0].axis('equal')

# Hiding the second subplot since we only need one pie chart
axarr[1].axis('off')

plt.tight_layout()
plt.show()