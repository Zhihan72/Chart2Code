import matplotlib.pyplot as plt

case_types = ['Property Law', 'Family Litigation', 'Trademark Cases', 'Workplace Policies', 'Civil Mediation']
shuffled_cases_resolved = [95, 60, 120, 50, 85]
single_color = '#6fa3ef'

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(case_types, shuffled_cases_resolved, color=single_color)

ax.set_title("Legal Insights: Yearly Case Handling Summary", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Resolved Cases Count', fontsize=12)

plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()