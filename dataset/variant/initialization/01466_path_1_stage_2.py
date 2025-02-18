import matplotlib.pyplot as plt

# Define the data with additional genres
genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Blues']
market_share = [25, 18, 20, 15, 7, 5, 6, 4, 3, 2]

# Extend color palette for new genres
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f0e442', '#ffb3e6', 
          '#c2f0c2', '#ff6666', '#d3a3ff', '#a3e1ff']

# Update explode to focus on multiple genres
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
    explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 10},
    pctdistance=0.85,
)

# Draw a white circle in the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')  

for text in texts + autotexts:
    text.set_color('black')

ax.set_title(
    "Distribution of Popular Music Genres\nin Streaming Services (2023)",
    fontsize=14, fontweight='bold', pad=20
)

ax.legend(genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

plt.tight_layout()
plt.show()