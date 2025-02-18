import matplotlib.pyplot as plt
import squarify

# Shortened group labels
sectors = ['Residential', 'Commercial', 'Industrial', 'Public', 'Transport']

# Data adjusted to match shorter labels while maintaining structure
data = {
    'Residential': [20, 50, 10, 20],
    'Commercial': [10, 20, 30, 40],
    'Industrial': [50, 25, 15, 10],
    'Public': [40, 20, 30, 10],
    'Transport': [40, 10, 20, 30]
}

sizes = []
for sector in sectors:
    sizes.extend(data[sector])

# Unified color for simplicity
single_color = '#FFD700'

plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, color=[single_color] * len(sizes), alpha=0.7, edgecolor="grey", linewidth=1.5)

plt.axis('off')
plt.tight_layout()
plt.show()