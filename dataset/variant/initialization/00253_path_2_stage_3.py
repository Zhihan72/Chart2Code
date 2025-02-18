import matplotlib.pyplot as plt

case_types = ['Employment Law', 'Corporate Compliance', 'Family Law', 'Intellectual Property', 'Contract Disputes']
cases_resolved = [60, 50, 85, 120, 95]
colors = ['#f76f8e', '#ffcc66', '#9d66cc', '#8ed372', '#6fa3ef']

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