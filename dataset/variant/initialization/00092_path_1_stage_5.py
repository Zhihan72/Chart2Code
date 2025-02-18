import matplotlib.pyplot as plt

practices = ['Composting', 'Recycling', 'Water Conservation', 'Energy-saving']
percentages = [30, 25, 15, 10]
colors = ['#FFD700', '#76C7C0', '#FF6F61', '#6B8E23']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=45,  # Changed the start angle for stylistic variety.
    labels=practices,
    autopct='%1.1f%%',
    shadow=False,  # Removed shadow for a flat look.
    explode=(0.1, 0.05, 0, 0.1)  # Randomly varied explode values.
)

ax.axis('equal')

plt.title('Green Efforts Distribution\nAcross City', size=14, color='darkred', loc='right', pad=20)  # Modified title style.
# Removed the legend to change an element dynamically.

for autotext in autotexts:
    autotext.set_color('darkred')  # Altered color for stylistic contrast.
    autotext.set_weight('normal')  # Changed weight of the text.

plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Added grid lines for enhancement.
plt.tight_layout()

plt.show()