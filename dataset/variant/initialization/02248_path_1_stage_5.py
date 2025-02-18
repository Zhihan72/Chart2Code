import matplotlib.pyplot as plt
import numpy as np

activities = ['Work', 'Exer.', 'Eat', 'Family', 'Sleep']
hours = np.array([8, 1, 2, 3, 5])
single_color = '#FF6F61'

fig, ax = plt.subplots(figsize=(9, 9))

explode = [0.1 if activity == 'Work' else 0.05 for activity in activities]
wedges, texts, autotexts = ax.pie(hours, labels=activities, autopct='%1.1f%%', 
                                  startangle=140, colors=[single_color] * len(activities), 
                                  explode=explode, wedgeprops=dict(width=0.3))

plt.setp(texts, size=12, fontweight='semibold')
plt.setp(autotexts, size=10, color='white')

ax.set_aspect('equal')
plt.title("Daily Routine", fontsize=16, fontweight='bold', y=1.05)

plt.tight_layout()
plt.show()