import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Blues']
market_share = [25, 18, 20, 15, 7, 5, 6, 4, 3, 2]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f0e442', '#ffb3e6', 
          '#c2f0c2', '#ff6666', '#d3a3ff', '#a3e1ff']
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, colors=colors, autopct='', startangle=140,
    explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'},
    pctdistance=0.85,
)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.tight_layout()
plt.show()