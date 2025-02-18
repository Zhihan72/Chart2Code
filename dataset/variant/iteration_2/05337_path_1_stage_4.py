import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

alice_running = [50, 52, 55, 60, 58, 62, 65, 68, 72, 75, 80, 85]
bob_running = [40, 45, 47, 50, 52, 55, 57, 60, 65, 70, 75, 80]
charlie_running = [30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75, 80]
danny_running = [25, 30, 35, 40, 45, 50, 55, 60, 63, 67, 72, 78]  # New data series for Danny

fig, ax1 = plt.subplots(figsize=(8, 6))
fig.suptitle('Health and Fitness Journey Over a Year', fontsize=16, style='italic', color='darkgreen')

ax1.plot(months, alice_running, marker='x', linestyle='--', color='blue', label='Alice Data')
ax1.plot(months, bob_running, marker='d', linestyle='-', color='orange', label='Bob Data')
ax1.plot(months, charlie_running, marker='p', linestyle=':', color='red', label='Charlie Data')
ax1.plot(months, danny_running, marker='o', linestyle='-.', color='green', label='Danny Data')  # Plotting Danny's data

ax1.set_title('Monthly Running Distances', fontsize=14, style='oblique', color='maroon')
ax1.set_xlabel('Months in Year', fontsize=12, color='teal')
ax1.set_ylabel('Running Distance (km)', fontsize=12, color='navy')
ax1.grid(color='gray', linestyle='-', linewidth=0.7, alpha=0.3)
ax1.legend(loc='lower right', fontsize=10, frameon=True, shadow=True, borderpad=1)

plt.tight_layout()
plt.show()