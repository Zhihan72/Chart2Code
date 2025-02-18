import matplotlib.pyplot as plt
import numpy as np

genres = [
    'Mystery/Thriller', 
    'Science Fiction/Fantasy', 
    'Fiction', 
    'Young Adult', 
    'Romance', 
    'Historical', 
    'Non-Fiction'
]

popularity = [15, 15, 25, 7, 10, 8, 20]

single_color = 'skyblue'

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=['Category {0}\n{1}%'.format(i + 1, pop) for i, pop in enumerate(popularity)], 
    colors=[single_color] * len(genres),  
    autopct=lambda p: f'{p:.1f}%', 
    startangle=120,
    pctdistance=0.8, 
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

ax.text(0, 0, 'Books\n2023\nData', horizontalalignment='center',
        verticalalignment='center', fontsize=12, weight='bold', color='gray')

ax.set_title('Genre Statistics\nFascinating Insights 2023', fontsize=14, weight='bold', pad=20)

ax.legend(
    wedges, 
    ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5', 'Type 6', 'Type 7'], 
    title="Categories", 
    title_fontsize='13', 
    fontsize='11', 
    loc='center left', 
    bbox_to_anchor=(1, 0.5),
    frameon=False
)

plt.tight_layout()
plt.show()