import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the average daily step counts of different age groups over a year. This data can be helpful for fitness instructors and healthcare professionals to understand how active different age groups are.

# Age groups (in years) and their corresponding average daily step count
age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80])
average_steps = np.array([12000, 15500, 14500, 13000, 11000, 9000, 7000, 4000])

# Months for the subplot with bar chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
steps_per_month = np.array([
    [11000, 16000, 15000, 14000, 11000, 10000, 8000, 5000, 6000, 7000, 7500, 8000], # Age 10
    [12000, 17000, 15500, 14500, 12000, 10500, 9000, 6000, 6500, 7500, 8000, 8500], # Age 20
    [12500, 16500, 14800, 13800, 11500, 9500, 8500, 5500, 6200, 7000, 7600, 8200],  # Age 30
    [11500, 15000, 14000, 13000, 10800, 9000, 7500, 5000, 5700, 6600, 7200, 7700],  # Age 40
    [10500, 14000, 13500, 12500, 10000, 8000, 7000, 4500, 5200, 6000, 6800, 7300],  # Age 50
    [9000, 12500, 11500, 10500, 8000, 7000, 6000, 3700, 4200, 5000, 5600, 6200],    # Age 60
    [7500, 10000, 9000, 8500, 6500, 5000, 4000, 2500, 3200, 4000, 4500, 4800],      # Age 70
    [4500, 7000, 6000, 5500, 4000, 3000, 2000, 1500, 1800, 2500, 2800, 3000]        # Age 80
])

# Set up the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(12, 12))

# Plot for average steps per day across age groups
ax[0].plot(age_groups, average_steps, 'o-', color='blue', linestyle='-', linewidth=2, markersize=8, markerfacecolor='red', markeredgewidth=2, markeredgecolor='darkred', label='Average Steps')

# Add title and labels, breaking title into lines if necessary
ax[0].set_title("Average Daily Step Counts\nAcross Age Groups Over a Year", fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel("Age (years)", fontsize=12)
ax[0].set_ylabel("Average Daily Steps", fontsize=12)

# Annotate significant points
for i in range(age_groups.size):
    ax[0].annotate(f'{average_steps[i]:,.0f}', xy=(age_groups[i], average_steps[i]), xytext=(-10, 10), textcoords='offset points', fontsize=10, color='black', bbox=dict(facecolor='yellow', edgecolor='none', pad=2))

# Customize grid lines and tick marks
ax[0].grid(True, which='both', linestyle='--', alpha=0.6)
ax[0].tick_params(axis='both', which='major', labelsize=10)

# Add a legend
ax[0].legend(loc='upper right', fontsize=10, frameon=True)

# Bar chart subplot for average steps per month for specific age groups
age_group_indices = [0, 1, 2, 3]  # Let's select age groups 10, 20, 30, 40
bar_width = 0.2  # Width of the bars
for idx, age_idx in enumerate(age_group_indices):
    ax[1].bar(np.arange(len(months)) + idx * bar_width, steps_per_month[age_idx], width=bar_width, label=f'Age {age_groups[age_idx]}')

# Adjust x-axis ticks to display months centered under the grouped bars
ax[1].set_xticks(np.arange(len(months)) + bar_width * 1.5)
ax[1].set_xticklabels(months)
ax[1].set_xlabel("Month", fontsize=12)
ax[1].set_ylabel("Average Daily Steps", fontsize=12)
ax[1].set_title("Monthly Average Daily Steps\nFor Selected Age Groups", fontsize=16, fontweight='bold', pad=20)

# Add a legend
ax[1].legend(loc='upper right', fontsize=10, frameon=True)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()