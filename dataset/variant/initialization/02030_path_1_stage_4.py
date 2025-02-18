import matplotlib.pyplot as plt
import numpy as np

beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]
colors = ['#8FD14F', '#FFD700', '#FF69B4', '#40E0D0', '#BA55D3']

# Randomly shuffle production volumes and colors while preserving the original dimensional structure
shuffled_indices = np.random.permutation(len(production_volumes))
production_volumes = [production_volumes[i] for i in shuffled_indices]
colors = [colors[i] for i in shuffled_indices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(beverages, production_volumes, color=colors, alpha=0.85, edgecolor='black')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.tight_layout()
plt.show()