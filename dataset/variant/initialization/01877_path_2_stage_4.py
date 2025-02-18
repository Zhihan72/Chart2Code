import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
popularity_scores_festival1 = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])
popularity_scores_festival2 = np.array([10, 18, 15, 6, 12, 25, 30, 20, 5, 8, 22, 11])

# Sort the scores and corresponding months for both festivals
sorted_indices_festival1 = np.argsort(popularity_scores_festival1)
sorted_scores_festival1 = popularity_scores_festival1[sorted_indices_festival1]

sorted_indices_festival2 = np.argsort(popularity_scores_festival2)
sorted_scores_festival2 = popularity_scores_festival2[sorted_indices_festival1]  # Align with festival 1 months

sorted_month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sorted_month_labels = [sorted_month_labels[i] for i in sorted_indices_festival1]

plt.figure(figsize=(12, 6))
bar_width = 0.35
indices = np.arange(len(sorted_month_labels))

plt.bar(indices, sorted_scores_festival1, bar_width, label='Town Festival', color='lightgreen', edgecolor='darkred', alpha=0.85, linestyle='--', hatch='/')
plt.bar(indices + bar_width, sorted_scores_festival2, bar_width, label='Seaside Festival', color='lightblue', edgecolor='darkblue', alpha=0.75, linestyle='--', hatch='\\')

plt.title("Festival Popularity in Harmony Bay\nby Month", fontsize=16, fontweight='bold', style='italic', color='darkgreen')
plt.xlabel("Month", fontsize=12, fontweight='light', color='grey')
plt.ylabel("Popularity Score", fontsize=12, fontweight='light', color='grey')
plt.xticks(indices + bar_width / 2, sorted_month_labels, rotation=60, fontsize=10, fontweight='medium', color='darkblue')
plt.yticks(fontsize=10, fontweight='medium', color='darkblue')
plt.grid(axis='y', color='grey', linestyle=':', linewidth=0.8)

plt.legend()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('grey')
plt.gca().spines['left'].set_color('grey')
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()