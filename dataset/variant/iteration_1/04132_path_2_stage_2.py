import matplotlib.pyplot as plt

crops = ['Barley', 'Vegetables', 'Corn', 'Soybeans', 'Oats', 'Rice', 'Wheat']
percentages = [25, 20, 15, 15, 10, 10, 5]

crop_colors = ['#FFD700', '#FFA500', '#8B4513', '#228B22', '#D2B48C', '#FFE4B5','#ADFF2F']

explode = [0.1 if crop == 'Barley' else 0 for crop in crops]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=['Barley', 'Veg', 'C', 'Soy', 'Oats', 'Rice', 'W'],
    colors=crop_colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2}
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.title("Crop Data Insights Revealed in Farmtown (2023)", fontsize=16, fontweight='bold', ha='center')

plt.legend(wedges, ['Barley', 'Veg', 'C', 'Soy', 'Oats', 'Rice', 'Wheat'], title="Produce", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()