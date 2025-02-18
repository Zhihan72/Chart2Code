import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are analyzing the nutrient content of different types of fruits gathered from diverse regions. 
# The study focuses on the distribution of Vitamin C content (in mg) per 100 grams of fruit.
# Fruits under consideration: Oranges, Strawberries, Kiwis, Lemons, and Pineapples

# Create data for Vitamin C content in mg per 100 grams for each fruit type
oranges = [53.2, 50.5, 52.4, 55.0, 54.3, 51.7, 52.8, 49.9, 54.1, 53.0]  # Vitamin C content for oranges
strawberries = [58.8, 59.4, 60.1, 57.5, 59.6, 58.0, 60.3, 61.2, 57.9, 59.8]  # Vitamin C content for strawberries
kiwis = [92.7, 93.0, 89.6, 95.4, 94.2, 91.1, 92.6, 90.8, 93.3, 92.0]  # Vitamin C content for kiwis
lemons = [77.0, 76.4, 78.2, 75.8, 77.7, 78.9, 76.1, 77.4, 75.6, 77.9]  # Vitamin C content for lemons
pineapples = [47.8, 48.2, 47.0, 49.3, 46.6, 47.4, 48.7, 47.5, 48.0, 48.8]  # Vitamin C content for pineapples

# Combine the data into a single list for the boxplot
data = [oranges, strawberries, kiwis, lemons, pineapples]

# Labels for the fruits
fruit_labels = ['Oranges', 'Strawberries', 'Kiwis', 'Lemons', 'Pineapples']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Create the box plot
box = ax.boxplot(data, vert=True, patch_artist=True, labels=fruit_labels, notch=True,
                 boxprops=dict(facecolor='#c6dbef', color='#084594'),
                 whiskerprops=dict(color='#084594'),
                 capprops=dict(color='#084594'),
                 medianprops=dict(color='#ef3b2c'),
                 flierprops=dict(marker='o', color='#ef3b2c', alpha=0.5))

# Customization of colors for each fruit type
colors = ['#d4e157', '#ffccbc', '#c5e1a5', '#ffab91', '#a5d6a7']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set the title, labels, and grid
ax.set_title("Vitamin C Content Across Different Fruits\n(measured in mg per 100 grams)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Types of Fruits", fontsize=12)
ax.set_ylabel("Vitamin C Content (mg)", fontsize=12)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding annotations for mean values for each fruit
for i, fruit in enumerate(data):
    mean_value = np.mean(fruit)
    ax.annotate(f'Mean: {mean_value:.1f}', xy=(i + 1, mean_value), xytext=(i + 1.2, mean_value + 5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, color='black')

# Automatically adjust layout for better fit and visibility
plt.tight_layout()

# Display the plot
plt.show()