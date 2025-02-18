import matplotlib.pyplot as plt

# Define video game genres
genres = ['Action', 'RPG', 'Sports', 'Strategy', 'Simulation', 'Puzzle']

# Randomly shuffled market shares to maintain structural integrity
market_shares = [15, 35, 7, 25, 10, 8]  # shuffled order

# Define colors aligned with genres
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#33FFFF', '#FFD700']

# Explode the position where Action was originally
explode = (0, 0.1, 0, 0, 0, 0)  # highlight shuffled genre

# Create a pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    market_shares, labels=genres, colors=colors, explode=explode, shadow=True,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85
)

# Enhance text visibility
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a circle at the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

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