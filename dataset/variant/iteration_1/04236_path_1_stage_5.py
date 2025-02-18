import matplotlib.pyplot as plt

regions = ['Oceania', 'S. America', 'Asia', 'Africa', 'Europe', 'N. America']
focuses = ['Quantum', 'Cybersec', 'AI', 'Renewable', 'Space', 'Biotech']
percentages = [25, 18, 20, 10, 15, 12]

colors = ['#3498DB', '#1ABC9C', '#9B59B6', '#E74C3C', '#F1C40F', '#2ECC71']

fig, ax = plt.subplots(figsize=(10, 8))

# Apply dashed line style, and different marker styles
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=False,  # Removed shadow for a flat design
    wedgeprops={'linestyle': '--'}  # Dashed border style
)

for i, text in enumerate(texts):
    text.set_text(f"{regions[i]} - {focuses[i]}")  # Combined region and focus in a single line
    text.set_size(8)  # Altered text size for thematic contrast
    text.set_color('grey')  # Altered text color

plt.setp(autotexts, size=10, weight='regular', color='black')  # Lightened on text weight

# Title with different font properties
ax.set_title("Ed. Focus Areas in 2075", fontsize=18, fontweight='light', pad=10)

# Altered legend location and title
ax.legend(wedges, regions, title="Regions", loc="upper right", handletextpad=0.5, bbox_to_anchor=(1.2, 1))

# Apply grid for improved readability
ax.grid(True, linestyle=':', linewidth=0.5)

plt.tight_layout()
plt.show()