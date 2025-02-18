import matplotlib.pyplot as plt
import numpy as np

activities = ['Family Time', 'Exercise', 'Work', 'Leisure', 'Meetings', 'Meals', 'Sleep']
hours = np.array([8, 2, 1, 2, 3, 3, 5])
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

fig, ax = plt.subplots(figsize=(9, 9))

explode = [0.1 if activity == 'Work' else 0.05 for activity in activities] 
wedges, texts, autotexts = ax.pie(
    hours, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    wedgeprops=dict(width=0.3)
)

plt.setp(texts, size=12, fontweight='semibold')
plt.setp(autotexts, size=10, color='white')

ax.set_aspect('equal')
plt.title("A Slice of Life:\nBalancing Remote Work and Play", fontsize=16, fontweight='bold', y=1.05)
ax.legend(wedges, activities, title="Daily Activities", loc="upper right", bbox_to_anchor=(1.3, 0.9))
plt.tight_layout()
plt.show()