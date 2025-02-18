import matplotlib.pyplot as plt
import numpy as np

hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes = tiredness_level * 20
colors = plt.cm.viridis(np.linspace(0, 1, len(hours_of_coding)))

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=colors, alpha=0.8, edgecolors='black', linewidth=1, cmap='viridis')

plt.tight_layout()
plt.show()