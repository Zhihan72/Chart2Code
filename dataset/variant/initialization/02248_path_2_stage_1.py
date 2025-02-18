import matplotlib.pyplot as plt
import numpy as np

activities = ['Work', 'Meetings', 'Exercise', 'Meals', 'Family Time', 'Leisure', 'Sleep']
hours = np.array([8, 2, 1, 2, 3, 3, 5])
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

fig, ax = plt.subplots(figsize=(9, 9))

# Modify the pie chart to a donut chart by setting a 'wedgeprops' dict with a width
explode = [0.1 if activity == 'Work' else 0.05 for activity in activities] 
wedges, texts, autotexts = ax.pie(
    hours, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    wedgeprops=dict(width=0.3)  # Add this parameter to create a donut chart
)

plt.setp(texts, size=12, fontweight='semibold')
plt.setp(autotexts, size=10, color='white')

ax.set_aspect('equal')
plt.title("Balancing Act:\nA Day in the Life of a Remote Worker", fontsize=16, fontweight='bold', y=1.05)
ax.legend(wedges, activities, title="Activities", loc="upper right", bbox_to_anchor=(1.3, 0.9))
plt.tight_layout()
plt.show()