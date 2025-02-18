import matplotlib.pyplot as plt

mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]

plt.figure(figsize=(6, 8))
box = plt.boxplot(mars_yields, vert=True, patch_artist=True, notch=True, whis=1.5)

# Set the appearance of the box without customizing
for patch in box['boxes']:
    patch.set_facecolor('#99FF99')  # Using a constant color

plt.ylabel("Metric Tons per Hectare", fontsize=12)

plt.tight_layout()
plt.show()