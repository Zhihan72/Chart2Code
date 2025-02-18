import matplotlib.pyplot as plt
import numpy as np

sleep_hours = np.array([9, 6, 10, 7, 8, 5])
productivity_scores = np.array([85, 65, 90, 70, 80, 60])

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(sleep_hours, productivity_scores, color='skyblue', edgecolor='k')

ax.set_xlabel('Productivity', fontsize=12)
ax.set_ylabel('Sleep (hrs)', fontsize=12)

plt.tight_layout()
plt.show()