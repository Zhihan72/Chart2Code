import matplotlib.pyplot as plt
import numpy as np

# Define programs and data (average daily steps)
programs = ['AM Fit', 'PM Yoga', 'WK Hiking', 'Dance', 'WorkWell', 'Stretch Class']
steps_data = [
    [8500, 8700, 7800, 9000, 8800, 8900, 8600, 9100, 9200, 8450],  # AM Fit
    [4500, 4200, 4100, 4600, 4700, 4900, 4300, 4800, 4400, 4550],  # PM Yoga
    [9500, 9600, 9400, 9300, 9200, 9800, 9900, 9700, 9350, 9600],  # WK Hiking
    [7000, 7500, 7200, 7100, 7350, 7600, 7800, 7400, 7500, 7350],  # Dance
    [5000, 4800, 4700, 5100, 5200, 5400, 4550, 4900, 5050, 5250],  # WorkWell
    [3000, 3200, 3100, 3300, 3250, 3100, 3150, 3400, 3350, 3450]   # Stretch Class
]

fig, ax = plt.subplots(figsize=(8, 6))

# Bar plot showing mean steps for each program
mean_steps = [np.mean(data) for data in steps_data]
ax.barh(programs, mean_steps, color='#ff9999', edgecolor='black')
ax.set_xlabel('Avg Steps', fontsize=12)
ax.set_title('Mean Steps by Program', fontsize=14, fontweight='bold', pad=20)
for i, v in enumerate(mean_steps):
    ax.text(v + 100, i, f'{v:.1f}', color='black', va='center', fontweight='bold')

plt.tight_layout()
plt.show()