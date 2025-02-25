import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

alice_running = [50, 52, 55, 60, 58, 62, 65, 68, 72, 75, 80, 85]
bob_running = [40, 45, 47, 50, 52, 55, 57, 60, 65, 70, 75, 80]
charlie_running = [30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75, 80]

fig, ax1 = plt.subplots(figsize=(8, 6))
fig.suptitle('Health and Fitness Journey Over a Year', fontsize=16, fontweight='bold', y=1.05)

ax1.plot(months, alice_running, marker='o', linestyle='-', color='purple', label='Alice')
ax1.plot(months, bob_running, marker='s', linestyle='--', color='purple', label='Bob')
ax1.plot(months, charlie_running, marker='^', linestyle='-.', color='purple', label='Charlie')
ax1.set_title('Monthly Running Distances', fontsize=14, fontweight='bold')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Running Distance (km)', fontsize=12)
ax1.grid(alpha=0.5, linestyle='--')
ax1.legend(loc='upper left')

plt.tight_layout()
plt.show()