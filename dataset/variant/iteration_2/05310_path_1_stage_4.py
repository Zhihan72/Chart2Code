import matplotlib.pyplot as plt
import squarify

# Original ecosystem labels have been randomly altered in order:
ecosystem_labels = [
    'Plankton\n(300k)', 'Fish\n(120k)', 'Echinoderms\n(70k)', 
    'Jellyfish\n(150k)', 'Cephalopods\n(100k)', 'Other Marine Species\n(90k)', 
    'Crustaceans\n(80k)', 'Mollusks\n(110k)'
]

populations = [150, 300, 100, 70, 80, 120, 110, 90]

single_color = '#1f77b4'

plt.figure(figsize=(14, 8))

# Plot with randomly altered labels
squarify.plot(sizes=populations, label=ecosystem_labels, color=[single_color]*len(populations), alpha=0.85, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=1.5)

plt.axis('off')

plt.tight_layout()

plt.show()