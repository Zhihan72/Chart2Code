import matplotlib.pyplot as plt
import numpy as np

# Altered genres and popularity by swapping positions of the second and fourth elements
genres = ['Sci-Fi', 'Fantasy', 'Romance', 'Mystery', 'Non-fic']
popularity = [30, 15, 25, 20, 10]

# Keeping the colors and explode list aligned with the altered genres
new_colors = ['#ff6f61', '#ba9ea0', '#fdae61', '#6baed6', '#b3de69'] 
explode = (0.1, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(popularity, labels=genres, colors=new_colors, autopct='%1.1f%%',
       startangle=140, explode=explode,
       wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

ax.set_title("Genre Popularity\n(Last 5 Yrs)", fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()