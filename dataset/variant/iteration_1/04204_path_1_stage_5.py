import matplotlib.pyplot as plt

# Data for Vitamin C content in mg per 100 grams for each fruit type
data = [
    [53.2, 50.5, 52.4, 55.0, 54.3, 51.7, 52.8, 49.9, 54.1, 53.0], # oranges
    [58.8, 59.4, 60.1, 57.5, 59.6, 58.0, 60.3, 61.2, 57.9, 59.8], # strawberries
    [92.7, 93.0, 89.6, 95.4, 94.2, 91.1, 92.6, 90.8, 93.3, 92.0], # kiwis
    [47.8, 48.2, 47.0, 49.3, 46.6, 47.4, 48.7, 47.5, 48.0, 48.8]  # pineapples
]

# Labels for the fruits
fruit_labels = ['Org', 'Str', 'Kiw', 'Pin']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Set a single color for all elements of the boxplot
color = 'blue'

# Create the horizontal box plot
ax.boxplot(data, vert=False, labels=fruit_labels, notch=True,
           boxprops=dict(color=color),
           whiskerprops=dict(color=color),
           capprops=dict(color=color),
           medianprops=dict(color=color),
           flierprops=dict(marker='o', color=color, alpha=0.5))

# Set the labels
ax.set_ylabel("Fruits", fontsize=12)
ax.set_xlabel("Vit C (mg)", fontsize=12)

# Remove grid, borders, and annotations
ax.set_frame_on(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Display the plot
plt.show()