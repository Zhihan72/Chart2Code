import numpy as np
import matplotlib.pyplot as plt

sectors = ['AI', 'Cloud Computing', 'Cybersecurity', 'IoT']
total_revenues = np.array([63, 45, 118, 90])
colors = ['#FFD700', '#4682B4', '#FF6347', '#32CD32']

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(sectors, total_revenues, color=colors)

ax.set_xlabel('Industries', fontsize=14)
ax.set_ylabel('Revenue (Billion USD)', fontsize=14)
ax.set_title('Revenue Overview by Industry', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()