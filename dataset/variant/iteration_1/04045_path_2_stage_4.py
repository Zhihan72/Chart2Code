import matplotlib.pyplot as plt

genres = ['Adventure', 'Simulation', 'Puzzle', 'Shooter', 'Sports']
market_share = [30, 25, 20, 15, 10]
new_colors = ['#FF6347', '#4682B4', '#D2691E', '#9ACD32', '#BA55D3']

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=45
)

plt.title('Game Genre Distribution - Forecast 2025', fontsize=18, fontweight='normal')
ax.legend(wedges, ['Adventure', 'Simulation', 'Puzzle', 'Shooter', 'Sports'], title="Category", loc="upper right")

plt.setp(autotexts, size=11, weight='normal', color='navy')
plt.setp(texts, size=13)

plt.tight_layout()
plt.show()