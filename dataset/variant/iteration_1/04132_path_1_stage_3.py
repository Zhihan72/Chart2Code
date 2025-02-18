import matplotlib.pyplot as plt

# Crops produced in Harvestville and their respective percentages
percentages = [25, 20, 15, 15, 10, 10, 5, 12, 8]

# New set of colors for the crops
crop_colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#FFD700', '#7FFF00']

# Explode the largest crop section (Wheat)
explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=crop_colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()