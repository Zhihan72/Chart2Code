import matplotlib.pyplot as plt

activities = ['Sports', 'Music', 'Art', 'Reading', 'Gaming', 'Volunteering']
percentages1 = [25, 20, 15, 5, 25, 10]
percentages2 = [30, 10, 20, 15, 10, 15]
hours_spent = [5, 3, 4, 2, 6, 3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode1 = (0, 0, 0, 0, 0.1, 0)
explode2 = (0, 0.1, 0, 0, 0, 0)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 8))

ax1.pie(
    percentages1,
    explode=explode1,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)

ax2.pie(
    percentages2,
    explode=explode2,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)

ax3.bar(activities, hours_spent, color=colors, edgecolor='black')

ax3.set_ylim(0, max(hours_spent) + 2)

plt.tight_layout()

plt.show()