import matplotlib.pyplot as plt

alpha_centauri_latency = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15]

plt.figure(figsize=(6, 8))
plt.boxplot(alpha_centauri_latency, vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# Randomly altered text elements for the chart
plt.ylabel('Response Duration (mins)')
plt.yticks(fontsize=10)
plt.xticks([1], ['Proxima Centauri Group'], fontsize=10)

plt.tight_layout()
plt.show()