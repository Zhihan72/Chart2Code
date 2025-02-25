import matplotlib.pyplot as plt

activities = ['Work', 'Gaming', 'News', 'Shopping', 'Social', 'Education', 'Media', 'Fitness', 'Others']
percentages = [9, 6, 8, 14, 28, 9, 18, 3, 5]
# Manually shuffled colors list
colors = ['#99ff99', '#c2c2f0', '#f2ae72', '#ff9999', '#c7f0c2', '#d77fa1', '#66b3ff', '#ffb3e6', '#ffcc99']

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(activities, percentages, color=colors, edgecolor='black')

ax.set_title("What Do People Do Online in 2023?", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Usage Rate (%)", fontsize=12)

ax.invert_yaxis()

for i in range(len(activities)):
    ax.text(percentages[i] + 1, i, f'{percentages[i]}%', va='center', fontsize=10, weight='bold')

plt.tight_layout()
plt.show()