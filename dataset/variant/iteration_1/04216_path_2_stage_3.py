import matplotlib.pyplot as plt

handheld_gaming_consoles = ['Nintendo Switch', 'PlayStation Vita', 'Game Boy', 'PSP']
market_share = [55, 15, 10, 15]

colors = ['#c2c2f0', '#66b3ff', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=handheld_gaming_consoles, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0.1)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title("Handheld Gaming Consoles Market Share Overview\nAn Insight into Market Distribution", fontsize=16, fontweight='bold', pad=20)

plt.setp(texts, size=12, weight='bold', color='black')
plt.setp(autotexts, size=10, weight='bold', color='darkslategray')

plt.tight_layout()
plt.show()