import matplotlib.pyplot as plt

categories = [
    'Planetary Exploration', 
    'Space Telescopes', 
    'Human Spaceflight', 
    'Astronomical Research', 
    'Space Mining',
    'Mars Colonization',
    'Space Tourism'
]
interest = [25, 20, 18, 12, 8, 10, 7]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c2c2f0', '#ffb3e6']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    interest,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0.1, 0, 0, 0, 0, 0.1, 0),
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(12)

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

plt.tight_layout()
plt.show()