import matplotlib.pyplot as plt

activities = ['Sports', 'Music', 'Art', 'Reading', 'Gaming', 'Volunteering', 'Cooking', 'Traveling']
percentages1 = [25, 20, 15, 5, 25, 10, 10, 20]
hours_spent = [5, 3, 4, 2, 6, 3, 4, 7]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6']
explode1 = (0, 0, 0, 0, 0.1, 0, 0, 0)

# Sort the activities and hours_spent based on descending order of hours_spent
sorted_data = sorted(zip(hours_spent, activities, colors), reverse=True)
sorted_hours_spent, sorted_activities, sorted_colors = zip(*sorted_data)

fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(12, 8))

ax1.pie(
    percentages1,
    explode=explode1,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)

ax3.bar(sorted_activities, sorted_hours_spent, color=sorted_colors, edgecolor='black')
ax3.set_ylim(0, max(hours_spent) + 2)

plt.tight_layout()
plt.show()