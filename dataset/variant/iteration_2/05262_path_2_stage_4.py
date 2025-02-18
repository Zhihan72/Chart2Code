import matplotlib.pyplot as plt

categories = ['Fiction', 'Non-Fic', 'Sci-Fi', 'Fantasy', 'Bio']
distribution = [30, 20, 15, 15, 10]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    distribution, 
    labels=categories, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=60,  # Randomly altered the start angle for variation in chart orientation
    wedgeprops={'width': 0.4, 'edgecolor': 'k'}  # Changed edge color and width for distinction
)

for text in texts:
    text.set_fontsize(14)  # Changed fontsize for visibility difference
    text.set_fontweight('regular')  # Changed font weight

for autotext in autotexts:
    autotext.set_color('blue')  # Randomly chose a different color for percentage text
    autotext.set_fontsize(11)  # Slightly increased fontsize
    autotext.set_fontweight('regular')  # Changed font weight

ax.axis('equal')
ax.set_title('Book Genres - 2023', fontsize=18, fontweight='bold', pad=30)  # Made title larger and more spaced
ax.legend(wedges, categories, loc='upper right', bbox_to_anchor=(1, 1, 0.5, 0.5), title="Genres", fontsize='medium', title_fontsize='14')  # Randomly altered legend position and sizes
plt.grid(visible=True)  # Added a grid to the polar plot for a new stylistic element
plt.tight_layout()
plt.show()