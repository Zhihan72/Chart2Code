import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1920, 2030, 10)
temp_changes = [0.0, 0.1, 0.15, 0.2, 0.25, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2]

plt.figure(figsize=(14, 8))

plt.plot(decades, temp_changes, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Temp Shift')
plt.fill_between(decades, temp_changes, color='#FF5733', alpha=0.2)

for i in range(len(decades)):
    plt.text(decades[i], temp_changes[i]+0.02, f'{temp_changes[i]:.2f}°C', ha='center', fontsize=10)

plt.title('Century Climate Variations', fontsize=18, fontweight='bold')
plt.xlabel('Time Period', fontsize=14)
plt.ylabel('Temp Variance (℃)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=12)
plt.xticks(decades, rotation=45)
plt.tight_layout()
plt.show()