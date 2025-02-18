import matplotlib.pyplot as plt

# Data Setup
accessories = ['Cases', 'Protectors', 'Chargers', 'Headphones', 'Watches', 'Other']
revenues = [18, 12, 14, 20, 10, 6]

# Define colors for each slice
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues,
    labels=accessories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=180,  # Changed start angle
    wedgeprops={'linestyle': '--'}  # Changed border style
)

# Enhance text appearance
for text in texts:
    text.set_fontsize(11)  # Adjusted font size
    text.set_color('navy')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')  # Changed text color

# Add title
plt.title(
    "Mobile Accessories Revenue in 2023",
    fontsize=16,
    fontweight='bold',
    color='darkgreen',  # Changed color
    pad=15             # Adjusted padding
)

# Add legend
ax.legend(
    wedges,
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)],
    title="Accessories",
    loc="upper right",  # Changed legend location
)

plt.grid(True, linestyle='--', linewidth=0.5)  # Added grid with style
plt.show()