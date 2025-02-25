import matplotlib.pyplot as plt

# Data Setup
accessories = ['Cases', 'Protectors', 'Chargers', 'Headphones', 'Watches', 'Other']
revenues = [18, 12, 14, 20, 10, 6]

# Define colors for each slice
colors = ['#66b3ff'] * len(revenues)  # Consistent color for all slices

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues,
    labels=accessories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140
)

# Enhance text appearance
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Add title
plt.title(
    "Mobile Accessories Revenue in 2023",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    pad=20
)

# Add legend
ax.legend(
    wedges,
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)],
    title="Accessories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

plt.tight_layout()
plt.show()