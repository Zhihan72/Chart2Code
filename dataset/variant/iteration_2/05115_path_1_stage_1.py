import matplotlib.pyplot as plt
import numpy as np

categories = ['Human Spaceflight', 'Space Mining', 'Space Telescopes', 'Astronomical Research', 'Planetary Exploration']
interest = [20, 10, 25, 15, 30]

colors = ['#99ff99', '#ff6666', '#66b3ff', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    interest, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0, 0, 0, 0, 0.1),
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('normal')

ax.set_title(
    "Public Interest in Different Aspects of Space Missions (2023):\n"
    "A Survey by Space Exploration Agency",
    fontsize=16, fontweight='bold', pad=20
)

ax.legend(
    wedges, categories, 
    title="Interest Areas", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10, title_fontsize='12'
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

plt.tight_layout()
plt.show()