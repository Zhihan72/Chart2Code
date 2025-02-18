import matplotlib.pyplot as plt
import squarify

ecosystem_labels = [
    'Jellyfish\n(150k)', 'Plankton\n(300k)', 'Cephalopods\n(100k)', 
    'Echinoderms\n(70k)', 'Crustaceans\n(80k)', 'Fish\n(120k)', 
    'Mollusks\n(110k)', 'Other Marine Species\n(90k)'
]
populations = [150, 300, 100, 70, 80, 120, 110, 90]

colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

plt.figure(figsize=(14, 8))

squarify.plot(sizes=populations, label=ecosystem_labels, color=colors, alpha=0.85, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=1.5)

plt.axis('off')

plt.tight_layout()

plt.show()