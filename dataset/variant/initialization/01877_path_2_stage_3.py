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
plt.bar(sorted_month_labels, sorted_scores, color='lightgreen', edgecolor='darkred', alpha=0.85, linestyle='--', hatch='/')

plt.title("Festival Popularity in Harmony Bay\nby Month", fontsize=16, fontweight='bold', style='italic', color='darkgreen')
plt.xlabel("Month", fontsize=12, fontweight='light', color='grey')
plt.ylabel("Popularity Score", fontsize=12, fontweight='light', color='grey')
plt.xticks(rotation=60, fontsize=10, fontweight='medium', color='darkblue')
plt.yticks(fontsize=10, fontweight='medium', color='darkblue')
plt.grid(axis='y', color='grey', linestyle=':', linewidth=0.8)

# Add a border to the chart
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('grey')
plt.gca().spines['left'].set_color('grey')
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()