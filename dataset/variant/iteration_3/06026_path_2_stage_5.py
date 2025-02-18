import matplotlib.pyplot as plt

genres = ['Sci-Fi', 'Fantasy', 'Romance', 'Mystery', 'Non-fic']
popularity = [30, 15, 25, 20, 10]
new_colors = ['#ff6f61', '#ba9ea0', '#fdae61', '#6baed6', '#b3de69']
explode = (0.1, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=genres, colors=new_colors, autopct='%1.1f%%',
                                  startangle=140, explode=explode,
                                  wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

# Convert pie chart to donut chart by adding a circle at the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.set_title("Genre Popularity\n(Last 5 Yrs)", fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()