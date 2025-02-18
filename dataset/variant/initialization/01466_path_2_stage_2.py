import matplotlib.pyplot as plt

# Updated data with additional music genres
genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B', 'Reggae', 'Latin']
market_share = [23, 17, 18, 14, 6, 4, 5, 3, 3, 2]

# Updated color palette with additional colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f0e442', '#ffb3e6', '#c2f0c2', '#ff6666', '#ffb399', '#8fd9b6']

# Explode slices for emphasis on 'Pop' and 'Hip Hop'
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
    explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 10}
)

# Draw a circle at the center to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio for a circular pie chart
ax.axis('equal')

# Title with multiple lines for clarity
ax.set_title(
    "Distribution of Popular Music Genres\nin Streaming Services (2023)",
    fontsize=14, fontweight='bold', pad=20
)

# Legend configuration for the additional genres
ax.legend(genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

plt.tight_layout()
plt.show()