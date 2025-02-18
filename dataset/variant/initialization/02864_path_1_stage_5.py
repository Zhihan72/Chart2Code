import numpy as np
import matplotlib.pyplot as plt

# Adding new data for planets and cuisines
planets = ['Orion', 'Vega', 'Zog', 'Xena']
cuisines = ['Saturnine Snacks', 'Martian Treats', 'Venusian Desserts', 'Jovian Bites']

# Updated popularity scores to include new entries
popularity_scores = np.array([
    [80, 65, 70, 60],
    [60, 75, 95, 85],
    [70, 85, 90, 65],
    [55, 90, 75, 80],
])

# Flatten and sort popularity scores along with storing indices
flattened_scores = popularity_scores.flatten()
sorted_indices = np.argsort(flattened_scores)
sorted_scores = flattened_scores[sorted_indices]

# Mapping sorted indices to planet-cuisine pairs
sorted_pairs = [(planets[i // len(cuisines)], cuisines[i % len(cuisines)]) for i in sorted_indices]

# Extract the sorted names for plotting
labels = [f"{p} - {c}" for p, c in sorted_pairs]

plt.figure(figsize=(12, 6))
plt.bar(labels, sorted_scores, color=plt.cm.plasma(np.linspace(0, 1, len(sorted_scores))))

plt.xticks(rotation=45, ha='right')
plt.xlabel('Planet - Cuisine Pair')
plt.ylabel('Flavor Score (0 - 100)')
plt.title('Sorted Bar Chart of Flavor Scores (Extended Data)')
plt.tight_layout()
plt.show()