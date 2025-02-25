import numpy as np
import matplotlib.pyplot as plt

sectors = ['Cloud Computing', 'AI', 'IoT', 'Cybersecurity']
total_revenues = np.array([45, 63, 90, 118])
colors = ['#4682B4', '#FFD700', '#32CD32', '#FF6347']

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(sectors, total_revenues, color=colors)

ax.set_xlabel('Industries', fontsize=14)
ax.set_ylabel('Revenue (Billion USD)', fontsize=14)
ax.set_title('Revenue Overview by Industry', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()