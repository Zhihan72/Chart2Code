import matplotlib.pyplot as plt

crops = ['Barley', 'Vegetables', 'Corn', 'Soybeans', 'Oats', 'Rice', 'Wheat']
percentages = [25, 20, 15, 15, 10, 10, 5]

new_colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#FF69B4', '#8A2BE2', '#7FFFD4']

explode = [0.1 if crop in ['Barley', 'Soybeans'] else 0 for crop in crops]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=['Barley', 'Veg', 'Corn', 'Soy', 'Oats', 'Rice', 'Wheat'],
    colors=new_colors,  # Different colors for each crop
    autopct='%1.1f%%',
    startangle=90,  # Changed start angle
    explode=explode,
    shadow=False,  # Removed the shadow
    wedgeprops={'edgecolor': 'grey', 'linewidth': 1.5}  # Changed edge color and width
)

centre_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

plt.title("Crop Yields in Farmtown (2023)", fontsize=18, fontweight='bold', ha='center')

plt.legend(wedges, crops, title="Produce Types", loc='upper right', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()