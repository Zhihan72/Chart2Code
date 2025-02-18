import matplotlib.pyplot as plt

# Define video game genres
genres = ['Action', 'RPG', 'Sports', 'Strategy', 'Simulation', 'Puzzle']

# Market shares for each genre
market_shares = [15, 35, 7, 25, 10, 8]

# Colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#33FFFF', '#FFD700']

# Explode to highlight RPG genre
explode = (0, 0.1, 0, 0, 0, 0)

# Create a standard pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    market_shares, labels=genres, colors=colors, explode=explode, shadow=True,
    autopct='%1.1f%%', startangle=140
)

# Enhance text visibility
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Maintain equal aspect ratio
plt.axis('equal')

# Title
plt.title('Video Game Genre Market Share in 2023:\nA Snapshot of Industry Trends', fontsize=16, fontweight='bold', ha='center')

# Legend positioning
plt.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Adjust layout
plt.tight_layout()

# Display chart
plt.show()