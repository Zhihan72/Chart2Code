import matplotlib.pyplot as plt
import numpy as np

genres = ['Sci-Fi', 'Mystery', 'Romance', 'Fantasy', 'Non-fic']
popularity = [30, 20, 25, 15, 10]
new_colors = ['#ff6f61', '#6baed6', '#fdae61', '#ba9ea0', '#b3de69']
explode = (0.1, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=genres, colors=new_colors, autopct='%1.1f%%',
                                  startangle=140, explode=explode, shadow=True,
                                  wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

ax.set_title("Genre Popularity\n(Last 5 Yrs)", fontsize=14, fontweight='bold', pad=20)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)
plt.tight_layout()
plt.show()