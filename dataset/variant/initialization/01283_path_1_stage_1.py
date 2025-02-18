import matplotlib.pyplot as plt
import numpy as np

# Data representing communication latency times for different civilizations
alpha_centauri_latency = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15]
betelgeuse_latency = [25, 28, 30, 27, 22, 20, 24, 29, 26, 23]
vega_latency = [5, 6, 7, 8, 7, 6, 5, 9, 10, 8]
proxima_latency = [9, 11, 10, 13, 12, 8, 10, 11, 10, 12]
sirius_latency = [17, 16, 19, 18, 20, 22, 21, 19, 17, 18]

latency_data = [alpha_centauri_latency, betelgeuse_latency, vega_latency, proxima_latency, sirius_latency]
civilizations = ['Alpha Centauri', 'Betelgeuse', 'Vega', 'Proxima', 'Sirius']

plt.figure(figsize=(12, 6))
plt.boxplot(latency_data, vert=False, patch_artist=False, labels=civilizations)

plt.xlabel('Latency Time (minutes)')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

plt.show()