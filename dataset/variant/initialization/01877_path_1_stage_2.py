import numpy as np
import matplotlib.pyplot as plt

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
popularity_scores = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

sorted_indices = np.argsort(popularity_scores)[::-1]
sorted_months = months[sorted_indices]
sorted_popularity_scores = popularity_scores[sorted_indices]

max_radius = 10
radii = sorted_popularity_scores / sorted_popularity_scores.max() * max_radius

plt.figure(figsize=(11, 8))

# Randomly shuffle color and pattern variations
colors = plt.cm.cool(np.linspace(0, 1, len(months)))
patterns = ['-', '--', '-.', ':', '', '/', '\\', '|', '_', '+', 'x', 'o']

# Bar chart with varied styles
for i, (month, radius) in enumerate(zip(sorted_months, radii)):
    plt.barh(month, radius, color=colors[i], edgecolor=np.random.choice(['gray', 'black']),
             hatch=patterns[i % len(patterns)], alpha=0.7)

# Customize other elements with random styles
plt.xlabel('Normalized Popularity Scores')
plt.title("Festival Popularity in Harmony Bay by Month (Sorted)", fontsize=16, fontweight='bold')
plt.grid(visible=np.random.choice([True, False]), color='grey', linestyle=np.random.choice(['-', '--', ':']), linewidth=0.7, alpha=0.6)

plt.show()