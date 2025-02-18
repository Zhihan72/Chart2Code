import matplotlib.pyplot as plt
import numpy as np

hours = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
cpu_usage = np.array([40, 45, 55, 70, 60, 65, 75, 70, 60, 50, 45])
ram_usage = np.array([30, 35, 40, 50, 45, 50, 55, 53, 48, 44, 40])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(hours, cpu_usage, color='purple', marker='o', linestyle='-', linewidth=2.5)
ax.plot(hours, ram_usage, color='orange', marker='s', linestyle='--', linewidth=2.5)

ax.set_xlabel("Hour of the Day", fontsize=14)
ax.set_ylabel("Usage (%)", fontsize=14)

for usage, color in zip([cpu_usage, ram_usage], ['purple', 'orange']):
    peak_hour = hours[np.argmax(usage)]
    peak_value = np.max(usage)
    ax.annotate(f'Peak: {peak_value}%', xy=(peak_hour, peak_value), xytext=(peak_hour, peak_value+5),
                arrowprops=dict(facecolor=color, shrink=0.05), fontsize=12, color=color, ha='center')

    low_hour = hours[np.argmin(usage)]
    low_value = np.min(usage)
    ax.annotate(f'Lowest: {low_value}%', xy=(low_hour, low_value), xytext=(low_hour, low_value-10),
                arrowprops=dict(facecolor=color, shrink=0.05), fontsize=12, color=color, ha='center')

plt.tight_layout()
plt.show()