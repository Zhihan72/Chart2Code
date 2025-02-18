import matplotlib.pyplot as plt
import numpy as np

# Data for the survey
creatures = ['Dragons', 'Unicorns', 'Phoenixes', 'Mermaids']
popularity = [40, 25, 20, 10]

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
wedges, texts, autotexts = ax.pie(popularity, colors=colors, labels=creatures, autopct='%1.1f%%', 
                                  startangle=90, pctdistance=0.85, explode=[0.2, 0, 0, 0.1])

# Annotation styling
for i, (pct, txt) in enumerate(zip(autotexts, texts)):
    txt.set_fontsize(11)
    if creatures[i] == 'Unicorns':
        txt.set_fontweight('bold')
        txt.set_color('#8c564b')
    pct.set_fontsize(11)
    pct.set_color('navy')

plt.title("Favorite Mythical Creatures", fontsize=18, fontweight='heavy', pad=15)
plt.setp(autotexts, size=11, weight="light", color="grey")

# Create a 'donut' appearance
centre_circle = plt.Circle((0,0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  

# Legend inside the chart area
ax.legend(wedges, creatures, title="Creatures", loc='upper left')

plt.show()