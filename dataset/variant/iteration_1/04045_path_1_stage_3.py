import matplotlib.pyplot as plt

# Updated data
genres = ['Racing', 'Adventure', 'Strategy', 'Puzzle']
market_share = [30, 25, 20, 15]
colors = ['#E24A33', '#348ABD', '#988ED5', '#777777']

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='white'),
    explode=(0.05, 0.05, 0.05, 0.05)
)

centre_circle = plt.Circle((0,0), 0.75, fc='white')
fig.gca().add_artist(centre_circle)

plt.setp(autotexts, size=10, color='black')
plt.setp(texts, size=12)

# Randomly altering textual elements:
plt.title("Video Game Genre Popularity")
plt.xlabel("Demographics")
plt.ylabel("Percentage")

plt.show()