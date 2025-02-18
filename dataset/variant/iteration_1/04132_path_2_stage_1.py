import matplotlib.pyplot as plt

# Crops produced in Harvestville and their respective percentages
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans', 'Oats', 'Rice', 'Vegetables']
percentages = [25, 20, 15, 15, 10, 10, 5]

# Colors associated with each crop
crop_colors = ['#FFD700', '#FFA500', '#8B4513', '#228B22', '#D2B48C', '#FFE4B5','#ADFF2F']

# Explode the largest crop section (Wheat)
explode = [0.1 if crop == 'Wheat' else 0 for crop in crops]

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=crops,
    colors=crop_colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2}
)

# Add a circle at the center to turn the pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.title("Annual Crop Production Distribution in Harvestville (2022)", 
          fontsize=16, fontweight='bold', ha='center')

plt.legend(wedges, crops, title="Crops", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()