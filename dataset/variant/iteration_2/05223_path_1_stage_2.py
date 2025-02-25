import matplotlib.pyplot as plt
import numpy as np

# Yields of different vegetables in kilograms with manually altered content
tomatoes = np.array([60, 55, 58, 65, 62, 64, 50, 70, 75, 80])  # Manually shuffled
carrots = np.array([49, 42, 50, 47, 40, 52, 45, 55, 58, 60])   # Manually shuffled
cucumbers = np.array([37, 32, 35, 30, 38, 40, 42, 45, 48, 50]) # Manually shuffled
lettuce = np.array([20, 28, 24, 26, 32, 30, 22, 34, 36, 38])   # Manually shuffled

# Calculate total yields (unchanged)
total_yields = {
    'Tomatoes': np.sum(tomatoes),
    'Carrots': np.sum(carrots),
    'Cucumbers': np.sum(cucumbers),
    'Lettuce': np.sum(lettuce)
}

# Sort data in descending order (unchanged)
sorted_vegetables = sorted(total_yields.items(), key=lambda item: item[1], reverse=True)

# Unpack sorted vegetables and their yields (unchanged)
vegetable_names, sorted_totals = zip(*sorted_vegetables)

# Setup the main plot (unchanged)
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for sorted vegetable yields (unchanged)
ax.bar(vegetable_names, sorted_totals, color=['tomato', 'orange', 'green', 'lightgreen'])

# Titles and labels (unchanged)
ax.set_title('Total Yields of Vegetables (2011-2020)', fontsize=16, fontweight='bold')
ax.set_ylabel('Total Yield (kg)', fontsize=12)
ax.set_xticks(range(len(vegetable_names)))
ax.set_yticks(np.arange(0, 700, 50))
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout (unchanged)
plt.tight_layout()

# Display the plot (unchanged)
plt.show()