import matplotlib.pyplot as plt
import squarify

populations = [110, 150, 70, 80, 300, 90, 120, 100]

# Use a single color for all groups
single_color = '#2f4b7c'
colors = [single_color] * len(populations)

plt.figure(figsize=(14, 8))

squarify.plot(sizes=populations, color=colors, alpha=0.85, edgecolor="white", linewidth=1.5)

plt.axis('off')
plt.show()