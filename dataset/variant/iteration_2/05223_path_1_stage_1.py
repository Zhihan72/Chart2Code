import matplotlib.pyplot as plt
import numpy as np

# Yields of different vegetables in kilograms
tomatoes = np.array([50, 55, 60, 58, 62, 64, 65, 70, 75, 80])
carrots = np.array([40, 42, 45, 47, 49, 52, 50, 55, 58, 60])
cucumbers = np.array([30, 32, 35, 37, 38, 40, 42, 45, 48, 50])
lettuce = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

# Calculate total yields
total_yields = {
    'Tomatoes': np.sum(tomatoes),
    'Carrots': np.sum(carrots),
    'Cucumbers': np.sum(cucumbers),
    'Lettuce': np.sum(lettuce)
}

# Sort data in descending order
sorted_vegetables = sorted(total_yields.items(), key=lambda item: item[1], reverse=True)

# Unpack sorted vegetables and their yields
vegetable_names, sorted_totals = zip(*sorted_vegetables)

# Setup the main plot
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for sorted vegetable yields
ax.bar(vegetable_names, sorted_totals, color=['tomato', 'orange', 'green', 'lightgreen'])

# Titles and labels
ax.set_title('Total Yields of Vegetables (2011-2020)', fontsize=16, fontweight='bold')
ax.set_ylabel('Total Yield (kg)', fontsize=12)
ax.set_xticks(range(len(vegetable_names)))
ax.set_yticks(np.arange(0, 700, 50))
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()