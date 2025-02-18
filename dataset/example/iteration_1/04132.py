import matplotlib.pyplot as plt

# Backstory:
# We're examining a small, thriving independent community of farmers called "Harvestville".
# The pie chart will represent the division of various crops produced in the community's annual agricultural report.

# Crops produced in Harvestville and their respective percentages
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans', 'Oats', 'Rice', 'Vegetables']
percentages = [25, 20, 15, 15, 10, 10, 5]

# Colors associated with each crop
crop_colors = ['#FFD700', '#FFA500', '#8B4513', '#228B22', '#D2B48C', '#FFE4B5','#ADFF2F']

# Explode the largest crop section (Wheat)
explode = [0.1 if crop == 'Wheat' else 0 for crop in crops]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=crops,
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

# Add a multi-line title for better clarity
plt.title("Annual Crop Production Distribution in Harvestville (2022)", 
          fontsize=16, fontweight='bold', ha='center')

# Add a legend for the crops
plt.legend(wedges, crops, title="Crops", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Show the plot
plt.show()