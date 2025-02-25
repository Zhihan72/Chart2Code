import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
productivity_software = np.array([73, 78, 80, 82, 85, 87, 86, 88, 90, 92, 94, 96])
productivity_hardware = np.array([65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 83, 85])
hours_worked = np.array([40, 42, 43, 45, 46, 47, 46, 48, 50, 52, 54, 55])

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.plot(months, productivity_software, 'o-', color='slateblue')
ax1.plot(months, productivity_hardware, 's--', color='orangered')

ax1.set_ylim(60, 100)
ax1.set_xticks(months)

ax2 = ax1.twinx()
ax2.plot(months, hours_worked, 'd-.', color='seagreen')
ax2.set_ylim(35, 60)

plt.tight_layout()
plt.show()