import matplotlib.pyplot as plt
import squarify

# Define the labels and their corresponding population values (in thousands)
ecosystem_labels = [
    'Jellyfish\n(110k)', 'Fish\n(150k)', 'Other Marine Species\n(70k)', 
    'Plankton\n(80k)', 'Crustaceans\n(300k)', 'Echinoderms\n(90k)', 
    'Mollusks\n(120k)', 'Cephalopods\n(100k)'
]
populations = [110, 150, 70, 80, 300, 90, 120, 100]  # Population values in thousands

# Define colors to represent each type of marine life, using a palette inspired by oceanic shades
colors = ['#665191', '#003f5c', '#ffa600', '#f95d6a', '#2f4b7c', '#ff7c43', '#a05195', '#d45087']

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