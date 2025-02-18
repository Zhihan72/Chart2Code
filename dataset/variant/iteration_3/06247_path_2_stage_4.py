import matplotlib.pyplot as plt

activities = ['Sports', 'Music', 'Art', 'Reading', 'Gaming', 'Volunteering']
percentages1 = [25, 20, 15, 5, 25, 10]  # Data for the first pie chart
percentages2 = [30, 10, 20, 15, 10, 15]  # Data for the second pie chart
hours_spent = [5, 3, 4, 2, 6, 3]  # Data for the bar chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode1 = (0.1, 0, 0, 0, 0.1, 0)  # Changed explosion for slices
explode2 = (0, 0, 0.1, 0, 0, 0)  # Changed explosion for slices

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 18))

# First pie chart
ax1.pie(
    percentages1,
    explode=explode1,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',  # Show percentage
    startangle=90,  # Alter start angle
    wedgeprops=dict(edgecolor='gray', linestyle='--', width=0.4),  # Change edge color and line style
    shadow=False
)
ax1.set_title('Activity Distribution 1')
ax1.legend(loc='upper right')  # Add legend

# Second pie chart
ax2.pie(
    percentages2,
    explode=explode2,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',  # Show percentage
    startangle=180,  # Different start angle
    wedgeprops=dict(edgecolor='blue', linestyle='-', width=0.4),  # Alter edge color and line style
    shadow=True
)
ax2.set_title('Activity Distribution 2')
ax2.legend(loc='lower right')  # Add legend

# Bar chart
ax3.bar(activities, hours_spent, color=colors, edgecolor='black', hatch='/')  # Add hatch to bars
ax3.set_xticklabels(activities, rotation=45, fontsize=10)
ax3.set_yticks(range(0, 8, 2))  # Set Y-tick positions
ax3.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)  # Add gridlines to the bar chart
ax3.set_ylabel('Hours')
ax3.set_title('Hours Spent on Activities')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()