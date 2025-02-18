import matplotlib.pyplot as plt

# Data for the favorite sci-fi franchises
franchises = ['Star Wars', 'Star Trek', 'Doctor Who', 'Dune', 'The Expanse', 'Others']
popularity_percentages = [30, 25, 15, 10, 10, 10]

# Define colors for each franchise
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#d3a6e0']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    labels=franchises,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9)
)

# Customize the text in wedges
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Set the title
plt.title('Favorite Science Fiction Franchises at Sci-Fi Convention 2023', fontsize=16, fontweight='bold', pad=20)

# Add legend
ax.legend(wedges, franchises, title="Franchises", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the pie chart is drawn as a circle
ax.set_aspect('equal')

# Automatically adjust layout for best presentation
plt.tight_layout()

# Display the chart
plt.show()