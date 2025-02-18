import matplotlib.pyplot as plt

# Data for video game genres and their market share percentages
genres = ['Action', 'RPG', 'Strategy', 'Sports', 'Shooter', 'Simulation', 'Adventure']
market_shares = [25, 20, 15, 15, 12, 8, 5]

# Colors and patterns for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']
patterns = ['/', '\\', '|', '-', '+', 'x', 'o']

# Explode parameter to highlight the 'Action' genre
explode = (0.1, 0.05, 0, 0, 0, 0, 0)

# Create the pie chart without stylistic elements
fig, ax = plt.subplots(figsize=(6, 6))

wedges, texts, autotexts = ax.pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, wedgeprops=dict(edgecolor='w', linewidth=1.5, alpha=0.9)
)

# Adding patterns to the wedges
for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')

ax.set_title('Market Share by Genre', fontsize=14, pad=15)
ax.axis('equal')

plt.tight_layout()
plt.show()