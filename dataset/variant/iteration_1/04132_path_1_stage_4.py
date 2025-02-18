import matplotlib.pyplot as plt

# Percentages of crops produced in Harvestville
percentages = [25, 20, 15, 15, 10, 10, 5, 12, 8]

# Colors representing different crops
crop_colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#FFD700', '#7FFF00']

# Explode the largest crop section
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
    wedgeprops={'edgecolor': 'black', 'width': 0.3}  # Added 'width' to create a donut chart
)

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.tight_layout()
plt.show()