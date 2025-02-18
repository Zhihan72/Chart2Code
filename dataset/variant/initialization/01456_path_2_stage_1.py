import matplotlib.pyplot as plt
import numpy as np

# Define years and brands
years = np.arange(2020, 2026)
brands = ['EcoChic', 'GreenThreads', 'SustainWear', 'NatureKnits', 'PureTrend']

# Eco-friendly materials data in tons
organic_cotton = np.array([
    [5, 10, 15, 20, 25, 30],   # EcoChic
    [4, 8, 12, 16, 20, 24],    # GreenThreads
    [6, 11, 17, 23, 29, 35],   # SustainWear
    [5, 9, 14, 18, 23, 28],    # NatureKnits
    [3, 7, 11, 15, 19, 23]     # PureTrend
])

recycled_polyester = np.array([
    [3, 5, 8, 12, 15, 19],     # EcoChic
    [4, 7, 11, 14, 18, 21],    # GreenThreads
    [2, 6, 9, 13, 17, 22],     # SustainWear
    [3, 5, 9, 13, 16, 20],     # NatureKnits
    [4, 6, 10, 14, 18, 22]     # PureTrend
])

hemp = np.array([
    [2, 4, 6, 8, 10, 12],      # EcoChic
    [1, 3, 5, 7, 9, 11],       # GreenThreads
    [3, 5, 8, 11, 14, 17],     # SustainWear
    [2, 4, 7, 10, 13, 15],     # NatureKnits
    [1, 2, 4, 6, 8, 10]        # PureTrend
])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Define bar width and positions
bar_width = 0.25
x_indexes = np.arange(len(years))
offset = bar_width * 3

# Colors for the materials
colors = ['#8E44AD', '#3498DB', '#2ECC71']  # Organic Cotton, Recycled Polyester, Hemp

# Plot grouped bars for each brand
for i, brand in enumerate(brands):
    ax.bar(x_indexes + i * offset, organic_cotton[i], width=bar_width, label='Organic Cotton' if i == 0 else "", color=colors[0], alpha=0.8)
    ax.bar(x_indexes + i * offset + bar_width, recycled_polyester[i], width=bar_width, label='Recycled Polyester' if i == 0 else "", color=colors[1], alpha=0.8)
    ax.bar(x_indexes + i * offset + bar_width * 2, hemp[i], width=bar_width, label='Hemp' if i == 0 else "", color=colors[2], alpha=0.8)

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Material Usage (Tons)', fontsize=12)
ax.set_title('Adoption of Eco-Friendly Materials in Fashion Brands\n(2020-2025)', fontsize=14, fontweight='bold', pad=20)

# Set x-ticks and x-tick labels
ax.set_xticks(x_indexes + 1.5 * bar_width)
ax.set_xticklabels(years)

# Adjust legend to avoid overlapping
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title='Material', ncol=1)

# Grid settings for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show plot
plt.show()