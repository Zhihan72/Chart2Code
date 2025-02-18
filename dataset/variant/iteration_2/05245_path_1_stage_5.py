import matplotlib.pyplot as plt

# Data Setup
accessories = ['Cases', 'Protectors', 'Chargers', 'Headphones', 'Watches', 'Other', 'Speakers', 'Cables']
revenues = [18, 12, 14, 20, 10, 6, 5, 8]

# Define colors for each slice
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#66ffb3']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues,
    labels=accessories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=180,
    wedgeprops={'linestyle': '--'}
)

# Enhance text appearance
for text in texts:
    text.set_fontsize(11)
    text.set_color('navy')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')

# Add title
plt.title(
    "Mobile Accessories Revenue in 2023",
    fontsize=16,
    fontweight='bold',
    color='darkgreen',
    pad=15
)

# Add legend
ax.legend(
    wedges,
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)],
    title="Accessories",
    loc="upper right",
)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()