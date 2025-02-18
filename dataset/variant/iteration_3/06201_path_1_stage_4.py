import matplotlib.pyplot as plt
import numpy as np

hours = np.arange(24)
cluster_A = [15, 13, 12, 10, 9, 7, 8, 10, 20, 30, 50, 70, 80, 85, 75, 70, 65, 60, 55, 50, 45, 40, 30, 20]
cluster_B = [10, 9, 8, 6, 5, 5, 6, 8, 18, 28, 48, 68, 78, 83, 73, 68, 63, 58, 53, 48, 43, 38, 28, 18]
cluster_C = [20, 18, 16, 14, 12, 10, 12, 15, 25, 35, 55, 75, 85, 88, 78, 72, 68, 64, 60, 55, 50, 45, 35, 25]
cluster_D = [12, 11, 10, 9, 8, 7, 8, 10, 22, 32, 52, 72, 82, 87, 77, 72, 67, 62, 57, 52, 47, 42, 32, 22]
average_cpu_usage = np.mean([cluster_A, cluster_B, cluster_C, cluster_D], axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(hours, cluster_A, color='cyan', linewidth=2, linestyle='-', label='A')
ax1.plot(hours, cluster_B, color='magenta', linewidth=2, linestyle='-.', label='B')
ax1.plot(hours, cluster_C, color='gold', linewidth=2, linestyle=':', label='C')
ax1.plot(hours, cluster_D, color='darkgreen', linewidth=2, linestyle='--', label='D')
ax1.plot(hours, average_cpu_usage, color='black', linestyle='-', linewidth=2, label='Avg')

ax1.set_title('CPU Utilization - 24H', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Hour', fontsize=12)
ax1.set_ylabel('Utilization (%)', fontsize=12)
ax1.set_xticks(hours)
ax1.set_xticklabels([f'{hour}:00' for hour in hours], rotation=45, ha='right')
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_yticklabels([f'{i}%' for i in range(0, 101, 10)])

peak_hours = [11, 12, 13]
for hour in peak_hours:
    ax1.axvline(x=hour, color='gray', linestyle='--', linewidth=1.2, alpha=0.7)
    ax1.text(hour, ax1.get_ylim()[1] * 0.98, f'Peak\n{hour}:00', ha='center', va='top', fontsize=9, color='black', fontweight='bold')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.grid(False)

ax1.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()