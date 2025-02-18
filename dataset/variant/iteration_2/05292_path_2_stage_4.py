import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
checkouts = np.array([1500, 2300, 2800, 3500, 4300, 6000, 7400, 8100, 7600, 6500, 4800, 2900])
stations = np.array([10, 15, 20, 25, 30, 35, 35, 40, 40, 40, 40, 40])
subscriptions = np.array([300, 450, 550, 700, 750, 900, 1000, 1050, 1100, 1150, 1200, 1250])
maintenance_calls = np.array([50, 60, 55, 40, 45, 65, 70, 85, 90, 80, 60, 55])

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(months, checkouts, color='blue', linestyle='-', marker='^', linewidth=2.5)

ax2 = ax1.twinx()
ax2.plot(months, stations, color='blue', linestyle='-.', marker='x', linewidth=1.5)
ax2.plot(months, subscriptions, color='blue', linestyle=':', marker='*', linewidth=3)
ax2.plot(months, maintenance_calls, color='blue', linestyle='--', marker='o', linewidth=2)

max_checkouts_month = months[np.argmax(checkouts)]
max_checkouts_value = max(checkouts)
ax1.annotate('',
             xy=(max_checkouts_month, max_checkouts_value), 
             xytext=(8, max_checkouts_value + 1500),
             arrowprops=dict(facecolor='grey', arrowstyle='->'))

ax1.grid(True, which='both', linestyle=':', linewidth=0.7)
ax2.grid(False)

plt.tight_layout()
plt.show()