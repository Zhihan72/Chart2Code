import matplotlib.pyplot as plt
import squarify

ecosystem_labels = [
    'Jellyfish\n(150k)', 'Plankton\n(300k)', 'Cephalopods\n(100k)', 
    'Echinoderms\n(70k)', 'Crustaceans\n(80k)', 'Fish\n(120k)', 
    'Mollusks\n(110k)', 'Other Marine Species\n(90k)'
]
populations = [150, 300, 100, 70, 80, 120, 110, 90]

single_color = '#1f77b4'

plt.figure(figsize=(14, 8))

squarify.plot(sizes=populations, label=ecosystem_labels, color=[single_color]*len(populations), alpha=0.85, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=1.5)

plt.axis('off')

plt.tight_layout()

plt.show()