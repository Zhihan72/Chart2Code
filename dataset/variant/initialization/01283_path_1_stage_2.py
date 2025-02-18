import matplotlib.pyplot as plt

# Data representing communication latency times for different civilizations
alpha_centauri_latency = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15]

# Create a basic vertical box plot for a single group of data
plt.figure(figsize=(6, 8))
plt.boxplot(alpha_centauri_latency, vert=True, patch_artist=False)

plt.ylabel('Latency Time (minutes)')
plt.yticks(fontsize=10)
plt.xticks([1], ['Alpha Centauri'], fontsize=10)

plt.tight_layout()

plt.show()