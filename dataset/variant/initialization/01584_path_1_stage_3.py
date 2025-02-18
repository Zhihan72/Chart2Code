import matplotlib.pyplot as plt
import numpy as np

popularity = [15, 15, 25, 7, 10, 8, 20]
single_color = 'skyblue'

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    popularity, 
    colors=[single_color] * len(popularity),  
    autopct=lambda p: f'{p:.1f}%', 
    startangle=120,
    pctdistance=0.8, 
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()