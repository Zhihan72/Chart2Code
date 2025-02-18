import matplotlib.pyplot as plt
import numpy as np

genres = ['Action', 'Role-Playing', 'Shooter', 'Sports', 'Puzzle']
market_share = [30, 25, 20, 15, 10]
new_colors = ['#FF6347', '#4682B4', '#D2691E', '#9ACD32', '#BA55D3']

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=45,  # Changed starting angle for interest
    pctdistance=0.80,  # Adjusted for a new look
    wedgeprops=dict(width=0.3, edgecolor='gray', linestyle='--'),  # Different edge styling
    explode=(0.03, 0.07, 0.05, 0.03, 0.02)  # Varied explode effect
)

centre_circle = plt.Circle((0,0), 0.70, fc='lightgrey') # Changed fill color
fig.gca().add_artist(centre_circle)

plt.title('Video Game Market Share by Genre - 2025', fontsize=18, fontweight='normal')  # Different styling
ax.legend(wedges, genres, title="Genres", loc="upper right")  # Altered legend position

plt.setp(autotexts, size=11, weight='normal', color='navy')  # Changed text color and style
plt.setp(texts, size=13)

plt.grid(linestyle='--', linewidth=0.5)  # Added grid lines for effect
plt.tight_layout()

plt.show()