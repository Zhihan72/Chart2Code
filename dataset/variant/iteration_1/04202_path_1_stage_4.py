import matplotlib.pyplot as plt

departments = ['Dev Team', 'Prod Mgmt', 'Ad Team', 'Sales Force']
num_employees = [50, 30, 20, 40]

sorted_indices = sorted(range(len(num_employees)), key=lambda i: num_employees[i], reverse=True)
sorted_departments = [departments[i] for i in sorted_indices]
sorted_employees = [num_employees[i] for i in sorted_indices]

# Altered color arrangement manually to shuffle
colors = ['palegreen', 'cornflowerblue', 'salmon', 'bisque']
sorted_colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(7.5, 7))
fig.suptitle('Company Division Insights', fontsize=16, fontweight='bold', y=1.02)

bars = ax.bar(sorted_departments, sorted_employees, color=sorted_colors, hatch='//')
ax.set_title('Team Size Comparison (Sorted)', fontsize=14)
ax.set_xlabel('Teams', fontsize=12)
ax.set_ylabel('Employees Count', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height - 3, '%d' % int(height), ha='center', va='bottom', color='darkred', fontsize=10)

plt.tight_layout()
plt.show()