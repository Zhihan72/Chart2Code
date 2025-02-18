import matplotlib.pyplot as plt

case_types = ['Corporate Compliance', 'Employment Law', 'Contract Disputes', 'Family Law', 'Intellectual Property']
cases_resolved = [50, 60, 95, 85, 120]
colors = ['#ffcc66', '#f76f8e', '#6fa3ef', '#9d66cc', '#8ed372']

# Sort data by cases resolved in ascending order
sorted_indices = sorted(range(len(cases_resolved)), key=lambda i: cases_resolved[i])
case_types = [case_types[i] for i in sorted_indices]
cases_resolved = [cases_resolved[i] for i in sorted_indices]
colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(case_types, cases_resolved, color=colors)

for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title("2022 Type Case Resolved: Legal Trend", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Case Type Variety', fontsize=12)
ax.set_ylabel('Resolved Cases Count', fontsize=12)
ax.spines[:].set_visible(False)
plt.xticks(rotation=15, ha='right', fontsize=10)
plt.tight_layout()
plt.show()