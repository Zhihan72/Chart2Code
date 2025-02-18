import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
popularity_scores = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

# Sort the scores and corresponding months in ascending order
sorted_indices = np.argsort(popularity_scores)
sorted_scores = popularity_scores[sorted_indices]
sorted_month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sorted_month_labels = [sorted_month_labels[i] for i in sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_month_labels, sorted_scores, color='lightblue', edgecolor='black', alpha=0.7)

plt.title("Festival Popularity in Harmony Bay\nby Month", fontsize=16, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Popularity Score")
plt.xticks(rotation=45)
plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()