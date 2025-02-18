import matplotlib.pyplot as plt

alpha_centauri_latency = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15]
beta_centauri_latency = [10, 13, 14, 11, 16, 15, 14, 13, 11, 13]
gamma_centauri_latency = [9, 11, 12, 10, 14, 13, 12, 11, 10, 12]

plt.figure(figsize=(8, 8))
data = [alpha_centauri_latency, beta_centauri_latency, gamma_centauri_latency]
plt.boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

plt.ylabel('Response Duration (mins)')
plt.yticks(fontsize=10)
plt.xticks([1, 2, 3], ['Proxima Centauri Group', 'Beta Centauri Group', 'Gamma Centauri Group'], fontsize=10)

plt.tight_layout()
plt.show()