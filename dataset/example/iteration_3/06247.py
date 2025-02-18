import matplotlib.pyplot as plt

# Data about students' preference for after-school activities
activities = ['Sports', 'Music', 'Art', 'Reading', 'Gaming', 'Volunteering']
percentages1 = [25, 20, 15, 5, 25, 10]
percentages2 = [30, 10, 20, 15, 10, 15]

# Number of hours students spend on these activities per week
hours_spent = [5, 3, 4, 2, 6, 3]

# Colors for each activity category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the 'Gaming' slice for emphasis in one of the pies
explode1 = (0, 0, 0, 0, 0.1, 0)
explode2 = (0, 0.1, 0, 0, 0, 0)

# Create a figure with three subplots (2 pie charts and 1 bar chart)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 8))

# Pie chart for younger students' after-school activities preferences
wedges1, texts1, autotexts1 = ax1.pie(
    percentages1,
    explode=explode1,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)
for autotext in autotexts1:
    autotext.set_color('black')
    autotext.set_fontsize(10)
ax1.set_title("Younger Students' Preferences", fontsize=14, fontweight='bold', pad=20)
ax1.legend(wedges1, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0.5))

# Pie chart for older students' after-school activities preferences
wedges2, texts2, autotexts2 = ax2.pie(
    percentages2,
    explode=explode2,
    labels=activities,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)
for autotext in autotexts2:
    autotext.set_color('black')
    autotext.set_fontsize(10)
ax2.set_title("Older Students' Preferences", fontsize=14, fontweight='bold', pad=20)
ax2.legend(wedges2, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0.5))

# Bar chart for average time spent on activities
bars = ax3.bar(activities, hours_spent, color=colors, edgecolor='black')
ax3.set_title("Average Weekly Time Spent\n on Activities (hours)", fontsize=14, fontweight='bold', pad=20)
ax3.set_xlabel("Activities")
ax3.set_ylabel("Hours per Week")
ax3.set_ylim(0, max(hours_spent) + 2)

# Adding value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval}', ha='center', va='bottom')

# Adjust layout to prevent text overlapping
plt.tight_layout()

# Show the plot
plt.suptitle("After-School Activities Preferences of Students", fontsize=18, fontweight='bold', y=1.02)
plt.show()