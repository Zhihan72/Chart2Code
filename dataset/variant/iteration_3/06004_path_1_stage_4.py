import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'])

temperatures = np.array([2, 3, 8, 15, 20, 25, 28, 27, 22, 16, 9, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, temperatures, color='red', marker='x', linestyle='--', linewidth=3, markersize=12)
ax1.tick_params(axis='y', colors='red')
ax1.set_ylim(0, 30)

ax1.set_xlabel('Months')
ax1.set_ylabel('Temperature (°C)', color='red')

ax1.legend(['Temperature'], loc='upper left', bbox_to_anchor=(0, 1), frameon=False)

plt.tight_layout()
plt.show()