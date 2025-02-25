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

# Manually shuffled the assigned colors
colors = ['#66b3ff', '#99ff99', '#ff9999', '#ffb3e6', '#ffcc99', '#c2c2f0', '#ff6666']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    interest,
    labels=categories,
    autopct='%1.1f%%',
    startangle=210,
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linewidth=2),
    explode=(0, 0.1, 0, 0.1, 0, 0, 0.1),
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('navy')
    autotext.set_fontsize(12)
    autotext.set_fontweight('normal')

for text in texts:
    text.set_fontsize(13)

ax.set_title(
    "Public Interest in Different Aspects of Space Missions (2023):\n"
    "A Survey by Space Exploration Agency",
    fontsize=18, fontweight='normal', pad=30
)

ax.legend(
    wedges, categories, 
    title="Interest Areas", loc='upper right', bbox_to_anchor=(1, 1),
    fontsize=11, title_fontsize='13'
)

ax.grid(True, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()