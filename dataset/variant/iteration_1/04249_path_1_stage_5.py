import matplotlib.pyplot as plt
import numpy as np

departments = ['Administration', 'Creative Team', 'Artistry', 'Tech Support']
work_hours = [35, 40, 42, 45]
stress_levels = [40, 50, 55, 75]
productivity = np.array([60, 70, 75, 80])

# Plot the bar chart for work hours
fig, ax1 = plt.subplots(figsize=(12, 8))
bars = ax1.bar(departments, work_hours, color='coral')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval} hrs", ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(departments, stress_levels, color='green', marker='o', linestyle='-', linewidth=2.5)

for i, level in enumerate(stress_levels):
    ax2.text(i, level + 2, f"{level}%", ha='center', va='bottom', color='green', fontsize=10)

ax1.set_title('Workload and Pressure in Various Office Divisions H1 2023', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Weekly Mean Workload (hrs)', fontsize=12)
ax1.set_xlabel('Divisions', fontsize=12)
ax2.set_ylabel('Pressure Metrics (%)', fontsize=12, color='green')

ax1.set_xticks(np.arange(len(departments)))
ax1.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

# Plot the bar chart for productivity
fig, ax3 = plt.subplots(figsize=(12, 4))
bars_prod = ax3.bar(departments, productivity, color='skyblue')

for i, value in enumerate(productivity):
    ax3.text(i, value + 1, f"{value}%", ha='center', va='bottom', color='skyblue', fontsize=10, fontweight='bold')

ax3.set_title('Efficiency Levels across Divisions in H1 2023', fontsize=14, fontweight='bold', pad=20)
ax3.set_ylabel('Efficiency (%)', fontsize=12)
ax3.set_xlabel('Divisions', fontsize=12)

ax3.set_xticks(np.arange(len(departments)))
ax3.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

plt.tight_layout()
plt.show()