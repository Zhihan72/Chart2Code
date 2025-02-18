import matplotlib.pyplot as plt

# Crops produced in Harvestville and their respective percentages
percentages = [25, 20, 15, 15, 10, 10, 5]

# Colors associated with each crop
crop_colors = ['#FFD700', '#FFA500', '#8B4513', '#228B22', '#D2B48C', '#FFE4B5','#ADFF2F']

# Explode the largest crop section (Wheat)
explode = [0.1, 0, 0, 0, 0, 0, 0]

# Create the pie chart without labels or titles
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=crop_colors,
    autopct='%1.1f%%',
    startangle=140,  # Start angle for better visual balance
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Show the plot
plt.show()