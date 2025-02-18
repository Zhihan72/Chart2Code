import matplotlib.pyplot as plt
import numpy as np

genres = ['Adventure', 'Simulation', 'Puzzle', 'Shooter', 'Sports']
market_share = [30, 25, 20, 15, 10]
new_colors = ['#FF6347', '#4682B4', '#D2691E', '#9ACD32', '#BA55D3']

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=45,
    pctdistance=0.80,
    wedgeprops=dict(width=0.3, edgecolor='gray', linestyle='--'),
    explode=(0.03, 0.07, 0.05, 0.03, 0.02)
)

centre_circle = plt.Circle((0,0), 0.70, fc='lightgrey')
fig.gca().add_artist(centre_circle)

plt.title('Game Genre Distribution - Forecast 2025', fontsize=18, fontweight='normal')
ax.legend(wedges, ['Adventure', 'Simulation', 'Puzzle', 'Shooter', 'Sports'], title="Category", loc="upper right")

plt.setp(autotexts, size=11, weight='normal', color='navy')
plt.setp(texts, size=13)

plt.grid(linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()