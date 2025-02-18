import matplotlib.pyplot as plt

genres = ['Racing', 'Adventure', 'Strategy', 'Puzzle']
market_share = [30, 25, 20, 15]
colors = ['#348ABD', '#777777', '#988ED5', '#E24A33']  # Manually shuffled

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90
)

plt.setp(autotexts, size=10, color='black')
plt.setp(texts, size=12)

plt.title("Video Game Genre Popularity")

plt.show()