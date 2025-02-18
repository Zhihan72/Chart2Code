import matplotlib.pyplot as plt

# Data for the favorite sci-fi franchises
popularity_percentages = [30, 25, 15, 10, 10, 10]

# Define colors for each franchise
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#d3a6e0']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9)
)

# Customize the text in wedges
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Ensure the pie chart is drawn as a circle
ax.set_aspect('equal')

# Automatically adjust layout for best presentation
plt.tight_layout()

# Display the chart
plt.show()