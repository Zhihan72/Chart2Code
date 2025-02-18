import numpy as np
import matplotlib.pyplot as plt

# Define months and corresponding festival popularity scores
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
popularity_scores = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

# Sort the popularity scores in descending order and obtain sorted indices
sorted_indices = np.argsort(popularity_scores)[::-1]
sorted_months = months[sorted_indices]
sorted_popularity_scores = popularity_scores[sorted_indices]

# Normalize sorted popularity scores for plotting
max_radius = 10
radii = sorted_popularity_scores / sorted_popularity_scores.max() * max_radius

# Plot bar chart
plt.figure(figsize=(10, 7))
plt.barh(sorted_months, radii, color=plt.cm.viridis(np.linspace(0, 1, len(months))), alpha=0.7, edgecolor='black')

# Customize plot
plt.xlabel('Normalized Popularity Scores')
plt.title("Festival Popularity in Harmony Bay by Month (Sorted)", fontsize=16, fontweight='bold')
plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

# Show the plot
plt.show()