import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart represents the progress of coffee consumption habits in different departments of a tech company. Over the past quarter, the amount of coffee consumed per week (in cups) varies within each department. The aim is to understand which departments have higher coffee consumption and how it varies.

# Data: Coffee consumption per week (in cups) in different departments over a quarter.
software_dept = [50, 55, 60, 62, 58, 65, 70, 72, 68, 74, 76, 80, 85]
hardware_dept = [30, 35, 40, 42, 38, 45, 50, 52, 48, 54, 56, 60, 65]
hr_dept = [10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 31, 34, 35]
marketing_dept = [20, 25, 30, 32, 28, 35, 40, 42, 38, 44, 46, 50, 55]
research_dept = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]

# Combine data into a list for the box plot
coffee_data = [software_dept, hardware_dept, hr_dept, marketing_dept, research_dept]

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the boxplot with specific customizations
bp = ax.boxplot(coffee_data, patch_artist=True, vert=True, notch=False,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='darkred', linewidth=2),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                flierprops=dict(marker='o', color='black', alpha=0.5, markersize=8))

# Assign a unique color to each box
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Adding scatter plots to show individual data points
for i, data in enumerate(coffee_data, start=1):
    y = np.array(data)
    x = np.random.normal(i, 0.04, size=len(y))  # jittering x position
    ax.scatter(x, y, alpha=0.6, edgecolor='w', s=50, label=f'{["Software", "Hardware", "HR", "Marketing", "Research"][i-1]} Points' if i == 1 else "")

# Setting up titles and labels
ax.set_title('Weekly Coffee Consumption Across Departments\nTechCorp Q3 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Departments', fontsize=14)
ax.set_ylabel('Coffee Consumption (Cups)', fontsize=14)
ax.set_xticks(np.arange(1, len(coffee_data) + 1))
ax.set_xticklabels(['Software', 'Hardware', 'HR', 'Marketing', 'Research'], rotation=15, fontsize=12)

# Adding grid for easier readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotate with the department's average consumption
for i, dept in enumerate(coffee_data, start=1):
    mean_val = np.mean(dept)
    ax.axhline(mean_val, ls='--', color=colors[i-1], alpha=0.7, linewidth=1.5, label=f'{["Software", "Hardware", "HR", "Marketing", "Research"][i-1]} Mean' if i == 1 else "")
    ax.text(i, mean_val + 1, f'{mean_val:.1f}', horizontalalignment='center', color=colors[i-1], fontsize=10)

# Adding a contextual note
ax.text(0.95, 0.02, "High coffee consumption in Research shows \n the intense work environment.", 
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))

# Adjust layout to prevent overlap
plt.tight_layout()

# Adding legend
ax.legend(loc='upper left', fontsize=9)

# Displaying the chart
plt.show()