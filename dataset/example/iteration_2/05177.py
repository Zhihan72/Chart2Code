import matplotlib.pyplot as plt
import numpy as np

# Define the backstory
# This chart shows the productivity levels of employees in an IT company over a span of one year.
# The data is collected on a monthly basis. Productivity is measured on a scale from 0 to 100.

# Define the months and productivity levels
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
productivity_software = np.array([73, 78, 80, 82, 85, 87, 86, 88, 90, 92, 94, 96])
productivity_hardware = np.array([65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 83, 85])

# Secondary y-axis data: Hours worked per week
hours_worked = np.array([40, 42, 43, 45, 46, 47, 46, 48, 50, 52, 54, 55])

# Create the plots
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot productivity levels for software development team
ax1.plot(months, productivity_software, 'o-', color='tab:blue', label='Software Team Productivity')
# Plot productivity levels for hardware development team
ax1.plot(months, productivity_hardware, 's--', color='tab:green', label='Hardware Team Productivity')

# Customize the first y-axis (productivity)
ax1.set_ylabel('Productivity Level (0-100)', fontsize=12)
ax1.set_ylim(60, 100)
ax1.set_xlabel('Months', fontsize=12)
ax1.set_xticks(months)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10)

# Add secondary y-axis for hours worked
ax2 = ax1.twinx()
ax2.plot(months, hours_worked, 'd-.', color='tab:red', label='Hours Worked per Week')
ax2.set_ylabel('Hours Worked per Week', fontsize=12)
ax2.set_ylim(35, 60)
ax2.legend(loc='upper right', fontsize=10)

# Add title and adjust layout to prevent overlap
plt.title('Monthly Productivity Levels and Hours Worked in an IT Company', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()

# Display the plot
plt.show()