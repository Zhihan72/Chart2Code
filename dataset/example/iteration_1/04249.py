import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart represents a fictional exploration of productivity levels and their effect on mental well-being in various departments within a tech company over the first half of 2023.

# Data for the bar chart
departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Design']
work_hours = [45, 40, 38, 35, 42]  # Average weekly work hours
stress_levels = [75, 50, 60, 40, 55]  # Stress levels out of 100

# Additional data for weekly productivity rates
productivity = np.array([80, 70, 65, 60, 75])  # Productivity out of 100

# Plotting the charts
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create bar chart for average work hours
bars = ax1.bar(departments, work_hours, color='skyblue', edgecolor='black', linewidth=0.8)

# Adding data labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval} hrs", ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

# Secondary y-axis for stress levels
ax2 = ax1.twinx()
ax2.plot(departments, stress_levels, color='coral', marker='o', linestyle='-', linewidth=2.5, label='Stress Levels (%)')

# Adding stress level labels
for i, level in enumerate(stress_levels):
    ax2.text(i, level + 2, f"{level}%", ha='center', va='bottom', color='coral', fontsize=10)

# Titles and labels
ax1.set_title('Exploring Work Hours vs Stress Levels in Tech Departments (H1 2023)', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Average Work Hours per Week', fontsize=12)
ax1.set_xlabel('Departments', fontsize=12)
ax2.set_ylabel('Stress Levels (%)', fontsize=12, color='coral')

# Set x-ticks and adjust x-labels to avoid overlap
ax1.set_xticks(np.arange(len(departments)))
ax1.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis of the bar chart
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Plotting subplots for productivity data
fig, ax3 = plt.subplots(figsize=(12, 4))
ax3.bar(departments, productivity, color='green', edgecolor='black', linewidth=0.8)

# Adding data labels above each bar
for i, value in enumerate(productivity):
    ax3.text(i, value + 1, f"{value}%", ha='center', va='bottom', color='green', fontsize=10, fontweight='bold')

# Titles and labels
ax3.set_title('Weekly Productivity Rates across Departments in H1 2023', fontsize=14, fontweight='bold', pad=20)
ax3.set_ylabel('Productivity (%)', fontsize=12)
ax3.set_xlabel('Departments', fontsize=12)

# Set x-ticks and adjust x-labels to avoid overlap
ax3.set_xticks(np.arange(len(departments)))
ax3.set_xticklabels(departments, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis of the productivity chart
ax3.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Final layout adjustment
plt.tight_layout()

# Display the plots
plt.show()