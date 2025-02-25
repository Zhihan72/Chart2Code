import matplotlib.pyplot as plt
import squarify

ecosystem_labels = [
    'Jellyfish\n(110k)', 'Fish\n(150k)', 'Other Marine Species\n(70k)', 
    'Plankton\n(80k)', 'Crustaceans\n(300k)', 'Echinoderms\n(90k)', 
    'Mollusks\n(120k)', 'Cephalopods\n(100k)'
]
populations = [110, 150, 70, 80, 300, 90, 120, 100]

# Use a single color for all groups
single_color = '#2f4b7c'
colors = [single_color] * len(populations)

plt.figure(figsize=(14, 8))
plt.title('Distribution of Marine Life in the Twilight Zone\n(200-1000 meters deep)', fontsize=16, fontweight='bold', pad=20)

squarify.plot(sizes=populations, label=ecosystem_labels, color=colors, alpha=0.85, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=1.5)

plt.axis('off')
plt.tight_layout()
plt.show()