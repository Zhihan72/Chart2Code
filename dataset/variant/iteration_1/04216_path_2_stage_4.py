import matplotlib.pyplot as plt

handheld_gaming_consoles = ['Game Boy', 'PSP', 'Nintendo Switch', 'PlayStation Vita']
market_share = [10, 15, 55, 15]

colors = ['#ffcc99', '#ff9999', '#c2c2f0', '#66b3ff']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=handheld_gaming_consoles, 
    autopct='%1.1f%%', 
    startangle=160, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0.1, 0)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title("Market Distribution of Gaming Consoles\nA Closer Look at Handheld Market Share", fontsize=16, fontweight='bold', pad=20)

plt.setp(texts, size=12, weight='bold', color='black')
plt.setp(autotexts, size=10, weight='bold', color='darkslategray')

plt.tight_layout()
plt.show()