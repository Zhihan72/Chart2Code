import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
departments = ['Tech Support', 'Creative Team', 'Negotiations', 'Administration', 'Artistry']
work_hours = [45, 40, 38, 35, 42]
stress_levels = [75, 50, 60, 40, 55]
productivity = np.array([80, 70, 65, 60, 75])

# Plotting the charts
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create bar chart for average work hours with shuffled color
bars = ax1.bar(departments, work_hours, color='coral', edgecolor='black', linewidth=0.8)

# Adding data labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval} hrs", ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

# Secondary y-axis for stress levels with shuffled color
ax2 = ax1.twinx()
ax2.plot(departments, stress_levels, color='green', marker='o', linestyle='-', linewidth=2.5, label='Stress Experience (%)')

# Adding stress level labels
for i, level in enumerate(stress_levels):
    ax2.text(i, level + 2, f"{level}%", ha='center', va='bottom', color='green', fontsize=10)

# Titles and labels
ax1.set_title('Workload and Pressure in Various Office Divisions H1 2023', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Weekly Mean Workload (hrs)', fontsize=12)
ax1.set_xlabel('Divisions', fontsize=12)
ax2.set_ylabel('Pressure Metrics (%)', fontsize=12, color='green')

# Set x-ticks and adjust x-labels to avoid overlap
ax1.set_xticks(np.arange(len(departments)))
ax1.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis of the bar chart
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Plotting subplots for productivity data with shuffled color
fig, ax3 = plt.subplots(figsize=(12, 4))
ax3.bar(departments, productivity, color='skyblue', edgecolor='black', linewidth=0.8)

# Adding data labels above each bar
for i, value in enumerate(productivity):
    ax3.text(i, value + 1, f"{value}%", ha='center', va='bottom', color='skyblue', fontsize=10, fontweight='bold')

# Titles and labels
ax3.set_title('Efficiency Levels across Divisions in H1 2023', fontsize=14, fontweight='bold', pad=20)
ax3.set_ylabel('Efficiency (%)', fontsize=12)
ax3.set_xlabel('Divisions', fontsize=12)

# Set x-ticks and adjust x-labels to avoid overlap
ax3.set_xticks(np.arange(len(departments)))
ax3.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis of the productivity chart
ax3.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Final layout adjustment
plt.tight_layout()

# Display the plots
plt.show()