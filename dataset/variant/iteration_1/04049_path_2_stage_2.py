import matplotlib.pyplot as plt

# Data: Vitamin C content (mg/100g) for different fruit groups
citrus_fruits = [53.2, 60.1, 90.8, 88.3, 80.5, 45.2, 49.8]
berries = [12.1, 58.8, 67.7, 21.3, 79.7, 14.5]
tropical_fruits = [61.1, 30.2, 36.4, 45.4, 52.4, 39.2, 55.8, 47.6]
stone_fruits = [6.6, 8.4, 10.3, 4.9, 11.9, 13.2]
pomes = [5.4, 14.3, 13.6, 10.1, 15.7]

# Compile data into a list
data = [citrus_fruits, berries, tropical_fruits, stone_fruits, pomes]
fruit_groups = ['Citrus Fruits', 'Berries', 'Tropical Fruits', 'Stone Fruits', 'Pomes']

# Create horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
box_colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5']

# Plot with custom box colors
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customize each box color
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Set y-axis labels to match the fruit groups
ax.set_yticklabels(fruit_groups, fontsize=11)
ax.set_xlabel('Vitamin C Content (mg/100g)', fontsize=12)

# Show plot
plt.show()