import matplotlib.pyplot as plt
import numpy as np

festival_labels = ['Harvest Festival', 'Music Festival', 'Art Festival', 'Literature Festival', 'Food Festival', 'Historical Reenactment']
festival_distribution = [25, 20, 15, 10, 20, 10]
festival_colors = ['#A5D4A0', '#FFABAB', '#92E4EB', '#D4A5A5', '#E7EFCF', '#FFC36C']
explode = (0, 0.1, 0, 0, 0.1, 0)

festival_names = ['Harvest Festival', 'Music Festival', 'Food Festival']
bar_colors = ['#D4A5A5', '#A5D4A0', '#FFC36C']
participants = [5000, 7000, 4500]

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

bars = ax[0].bar(festival_names, participants, color=bar_colors, edgecolor='black')
for bar in bars:
    yval = bar.get_height()
    ax[0].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=12)

ax[0].set_title("Participants in Top Festivals", fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel("Number of Participants")
ax[0].set_ylim(0, 8000)

wedges, texts, autotexts = ax[1].pie(
    festival_distribution, 
    labels=festival_labels, 
    colors=festival_colors, 
    explode=explode, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    shadow=True
)
plt.setp(autotexts, size=12, weight="bold", color='black')
plt.setp(texts, size=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax[1].set_title("Festival Distribution in Aveburrow", fontsize=16, fontweight='bold', pad=20)

fig.suptitle("Aveburrow Festivals Overview", fontsize=20, fontweight='bold',)

plt.tight_layout()
plt.show()