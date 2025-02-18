import numpy as np
import matplotlib.pyplot as plt

smart_thermostat = [2.1, 2.4, 2.3, 3.0, 3.5, 3.8, 4.0, 4.2, 4.1, 3.7, 3.4, 3.2]
smart_lighting = [1.2, 1.3, 1.5, 1.7, 2.0, 2.2, 2.4, 2.5, 2.3, 2.1, 1.8, 1.6]
smart_security = [3.0, 3.2, 3.1, 3.3, 3.5, 3.6, 3.8, 4.0, 4.1, 4.2, 4.3, 4.4]

data_usage = np.array([
    smart_thermostat,
    smart_lighting,
    smart_security
])

colors = ['orange', 'purple', 'green']  # Corresponding color for smart_refrigerator is removed

fig, ax = plt.subplots(figsize=(14, 8))

for idx in range(data_usage.shape[0]):
    ax.plot(data_usage[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx])

plt.tight_layout()
plt.show()