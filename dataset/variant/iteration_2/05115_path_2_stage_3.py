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
    startangle=210,  # Changed startangle for stylistic variation
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linewidth=2),  # Changed edge color and width
    explode=(0, 0.1, 0, 0.1, 0, 0, 0.1),  # Altered explode pattern
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('navy')  # Changed font color
    autotext.set_fontsize(12)  # Increased font size
    autotext.set_fontweight('normal')  # Changed font weight

for text in texts:
    text.set_fontsize(13)  # Changed label font size

ax.set_title(
    "Public Interest in Different Aspects of Space Missions (2023):\n"
    "A Survey by Space Exploration Agency",
    fontsize=18, fontweight='normal', pad=30  # Altered title font size and weight
)

ax.legend(
    wedges, categories, 
    title="Interest Areas", loc='upper right', bbox_to_anchor=(1, 1),  # Changed legend location
    fontsize=11, title_fontsize='13'
)

ax.grid(True, linestyle='--', linewidth=0.7)  # Added grid

plt.tight_layout()
plt.show()