import matplotlib.pyplot as plt
import squarify

# Backstory:
# Deep beneath the ocean, researchers are studying various marine ecosystems and their biodiversity. The data gathered helps illuminate the distribution of different types of marine life inhabiting the twilight zone (200-1000 meters deep).

# Define the labels and their corresponding population values (in thousands)
ecosystem_labels = [
    'Fish\n(120k)', 'Cephalopods\n(100k)', 'Jellyfish\n(150k)', 
    'Crustaceans\n(80k)', 'Mollusks\n(110k)', 'Plankton\n(300k)', 
    'Echinoderms\n(70k)', 'Other Marine Species\n(90k)'
]
populations = [120, 100, 150, 80, 110, 300, 70, 90]  # Population values in thousands

# Define colors to represent each type of marine life, using a palette inspired by oceanic shades
colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

# Create a new figure for the tree map
plt.figure(figsize=(14, 8))
plt.title('Distribution of Marine Life in the Twilight Zone\n(200-1000 meters deep)', fontsize=16, fontweight='bold', pad=20)

# Plot the tree map with squarify
squarify.plot(sizes=populations, label=ecosystem_labels, color=colors, alpha=0.85, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=1.5)

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust the layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()