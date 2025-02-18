import matplotlib.pyplot as plt
import numpy as np

# Define the case types and a shuffled set of resolved case counts
case_types = ['Contract Disputes', 'Employment Law', 'Intellectual Property', 'Corporate Compliance', 'Family Law']
cases_resolved = [95, 60, 120, 50, 85]  # Manually shuffled

colors = ['#6fa3ef', '#f76f8e', '#8ed372', '#ffcc66', '#9d66cc']

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(case_types, cases_resolved, color=colors, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title("Legal Department's Case Resolution by Type: 2022 Snapshot", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Type of Case', fontsize=12)
ax.set_ylabel('Number of Cases Resolved', fontsize=12)

plt.xticks(rotation=15, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()