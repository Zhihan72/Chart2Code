import matplotlib.pyplot as plt

activities = ['Volunteering', 'Music', 'Art', 'Reading', 'Sports', 'Gaming']
percentages1 = [25, 15, 10, 5, 25, 20]  # Altered data for the first pie chart
percentages2 = [20, 15, 15, 30, 10, 10]  # Altered data for the second pie chart
hours_spent = [3, 3, 4, 6, 5, 2]  # Altered data for the bar chart
colors = ['#ffb3e6', '#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0']
explode1 = (0, 0, 0, 0, 0.1, 0.1)  # Altered explosion for slices
explode2 = (0, 0.1, 0, 0, 0.1, 0)  # Altered explosion for slices

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 18))

# First pie chart
ax1.pie(
    percentages1,
    explode=explode1,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='gray', linestyle='--', width=0.4),
    shadow=False
)
ax1.set_title('Activity Distribution 1')
ax1.legend(loc='upper right')

# Second pie chart
ax2.pie(
    percentages2,
    explode=explode2,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',
    startangle=180,
    wedgeprops=dict(edgecolor='blue', linestyle='-', width=0.4),
    shadow=True
)
ax2.set_title('Activity Distribution 2')
ax2.legend(loc='lower right')

# Bar chart
ax3.bar(activities, hours_spent, color=colors, edgecolor='black', hatch='/')
ax3.set_xticklabels(activities, rotation=45, fontsize=10)
ax3.set_yticks(range(0, 8, 2))
ax3.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)
ax3.set_ylabel('Hours')
ax3.set_title('Hours Spent on Activities')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()