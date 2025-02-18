import matplotlib.pyplot as plt
import numpy as np

# Original case types and counts
case_types = ['Property Law', 'Family Litigation', 'Trademark Cases', 'Workplace Policies', 'Civil Mediation']
cases_resolved = [85, 95, 120, 60, 50]

# Shuffle the counts while preserving structure
shuffled_cases_resolved = [95, 60, 120, 50, 85]
single_color = '#6fa3ef'

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(case_types, shuffled_cases_resolved, color=single_color, edgecolor='black')

for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center', fontsize=10, fontweight='bold', color='black')

ax.set_title("Legal Insights: Yearly Case Handling Summary", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Resolved Cases Count', fontsize=12)
ax.set_ylabel('Case Categories', fontsize=12)

plt.yticks(fontsize=10)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()