import numpy as np
import matplotlib.pyplot as plt

# Data for months and popularity scores
months = np.array(['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
popularity_scores = np.array([10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

# Sort months based on popularity
sorted_indices = np.argsort(popularity_scores)[::-1]
sorted_months = months[sorted_indices]
sorted_popularity_scores = popularity_scores[sorted_indices]

# Calculate radii for plotting
max_radius = 10
radii = sorted_popularity_scores / sorted_popularity_scores.max() * max_radius

plt.figure(figsize=(11, 8))

colors = plt.cm.cool(np.linspace(0, 1, len(months)))
patterns = ['-', '--', '-.', ':', '', '/', '\\', '|', '_', '+', 'x', 'o']

# Plot the chart
for i, (month, radius) in enumerate(zip(sorted_months, radii)):
    plt.barh(month, radius, color=colors[i], edgecolor='black', hatch=patterns[i % len(patterns)], alpha=0.7)

plt.xlabel('Popularity')
plt.title("Harmony Bay Festival", fontsize=16, fontweight='bold')
plt.grid(visible=False, color='grey', linestyle='-', linewidth=0.7, alpha=0.6)

plt.show()