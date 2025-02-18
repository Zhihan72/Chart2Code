import matplotlib.pyplot as plt

crops = ['Vegetables', 'Rice', 'Corn', 'Oats', 'Wheat', 'Soybeans', 'Barley']
percentages = [10, 25, 20, 5, 15, 10, 15]

new_colors = ['#FF6347', '#FFD700', '#4682B4', '#FF69B4', '#7FFFD4', '#32CD32', '#8A2BE2']

explode = [0.1 if crop in ['Vegetables', 'Rice'] else 0 for crop in crops]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=['Veg', 'Rice', 'Corn', 'Oats', 'Wheat', 'Soy', 'Barley'],
    colors=new_colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    wedgeprops={'edgecolor': 'grey', 'linewidth': 1.5}
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