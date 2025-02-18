import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
departments = ['Eng', 'Mkt', 'Sales', 'HR', 'Dsgn']
work_hours = [45, 40, 38, 35, 42]  
stress_levels = [75, 50, 60, 40, 55]  

productivity = np.array([80, 70, 65, 60, 75])

fig, ax1 = plt.subplots(figsize=(12, 8))

bars = ax1.bar(departments, work_hours, color='coral', edgecolor='black', linewidth=0.8)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval}h", ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(departments, stress_levels, color='green', marker='o', linestyle='-', linewidth=2.5, label='Stress (%)')

for i, level in enumerate(stress_levels):
    ax2.text(i, level + 2, f"{level}%", ha='center', va='bottom', color='green', fontsize=10)

ax1.set_title('Work vs Stress in Tech (H1 2023)', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Avg Hours/Week', fontsize=12)
ax1.set_xlabel('Depts', fontsize=12)
ax2.set_ylabel('Stress (%)', fontsize=12, color='green')

ax1.set_xticks(np.arange(len(departments)))
ax1.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

fig, ax3 = plt.subplots(figsize=(12, 4))
ax3.bar(departments, productivity, color='skyblue', edgecolor='black', linewidth=0.8)

for i, value in enumerate(productivity):
    ax3.text(i, value + 1, f"{value}%", ha='center', va='bottom', color='skyblue', fontsize=10, fontweight='bold')

ax3.set_title('Productivity by Dept (H1 2023)', fontsize=14, fontweight='bold', pad=20)
ax3.set_ylabel('Prod. (%)', fontsize=12)
ax3.set_xlabel('Depts', fontsize=12)

ax3.set_xticks(np.arange(len(departments)))
ax3.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)
ax3.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

plt.tight_layout()
plt.show()