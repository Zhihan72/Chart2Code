import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

alice_running = [50, 52, 55, 60, 58, 62, 65, 68, 72, 75, 80, 85]
bob_running = [40, 45, 47, 50, 52, 55, 57, 60, 65, 70, 75, 80]
charlie_running = [30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75, 80]
alice_gym = [8, 10, 12, 15, 14, 16, 18, 20, 22, 23, 25, 27]
bob_gym = [5, 7, 9, 11, 13, 15, 16, 18, 20, 22, 24, 26]
charlie_gym = [4, 6, 8, 10, 11, 13, 15, 17, 18, 19, 20, 22]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('Health and Fitness Journey Over a Year', fontsize=16, fontweight='bold', y=1.05)

ax1.plot(months, alice_running, marker='o', linestyle='-', color='purple', label='Alice')
ax1.plot(months, bob_running, marker='s', linestyle='--', color='purple', label='Bob')
ax1.plot(months, charlie_running, marker='^', linestyle='-.', color='purple', label='Charlie')
ax1.set_title('Monthly Running Distances', fontsize=14, fontweight='bold')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Running Distance (km)', fontsize=12)
ax1.grid(alpha=0.5, linestyle='--')
ax1.legend(loc='upper left')

ax2.plot(months, alice_gym, marker='o', linestyle='-', color='purple', label='Alice')
ax2.plot(months, bob_gym, marker='s', linestyle='--', color='purple', label='Bob')
ax2.plot(months, charlie_gym, marker='^', linestyle='-.', color='purple', label='Charlie')
ax2.set_title('Monthly Gym Visits', fontsize=14, fontweight='bold')
ax2.set_xlabel('Months', fontsize=12)
ax2.set_ylabel('Gym Visits', fontsize=12)
ax2.grid(alpha=0.5, linestyle='--')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()