import matplotlib.pyplot as plt
import numpy as np

# Data for departments
departments = ['Eng', 'Mkt', 'Sales', 'HR', 'Dsgn', 'Ops']
work_hours = [45, 40, 38, 35, 42, 37]  
stress_levels = [75, 50, 60, 40, 55, 45]  
productivity = np.array([80, 70, 65, 60, 75, 68])

# Sort data based on work_hours (ascending)
sorted_indices = np.argsort(work_hours)
sorted_departments = [departments[i] for i in sorted_indices]
sorted_work_hours = [work_hours[i] for i in sorted_indices]
sorted_stress_levels = [stress_levels[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(12, 8))

bars = ax1.bar(sorted_departments, sorted_work_hours, color='coral')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval}h", ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(sorted_departments, sorted_stress_levels, color='green', marker='o', linestyle='-', linewidth=2.5)

for i, level in enumerate(sorted_stress_levels):
    ax2.text(i, level + 2, f"{level}%", ha='center', va='bottom', color='green', fontsize=10)

ax1.set_title('Work vs Stress in Tech (H1 2023)', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Avg Hours/Week', fontsize=12)
ax1.set_xlabel('Depts', fontsize=12)
ax2.set_ylabel('Stress (%)', fontsize=12, color='green')

ax1.set_xticks(np.arange(len(sorted_departments)))
ax1.set_xticklabels(sorted_departments, rotation=45, ha='right', fontsize=10)

# Sort data based on productivity (ascending)
sorted_indices_prod = np.argsort(productivity)
sorted_departments_prod = [departments[i] for i in sorted_indices_prod]
sorted_productivity = productivity[sorted_indices_prod]

fig, ax3 = plt.subplots(figsize=(12, 4))
ax3.bar(sorted_departments_prod, sorted_productivity, color='skyblue')

for i, value in enumerate(sorted_productivity):
    ax3.text(i, value + 1, f"{value}%", ha='center', va='bottom', color='skyblue', fontsize=10, fontweight='bold')

ax3.set_title('Productivity by Dept (H1 2023)', fontsize=14, fontweight='bold', pad=20)
ax3.set_ylabel('Prod. (%)', fontsize=12)
ax3.set_xlabel('Depts', fontsize=12)

ax3.set_xticks(np.arange(len(sorted_departments_prod)))
ax3.set_xticklabels(sorted_departments_prod, rotation=45, ha='right', fontsize=10)

plt.tight_layout()
plt.show()