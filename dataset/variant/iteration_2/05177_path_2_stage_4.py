import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Existing data
productivity_software = np.array([73, 78, 80, 82, 85, 87, 86, 88, 90, 92, 94, 96])
productivity_hardware = np.array([65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 83, 85])
hours_worked = np.array([40, 42, 43, 45, 46, 47, 46, 48, 50, 52, 54, 55])

# New data series
sales_growth = np.array([5, 6, 7, 8, 10, 12, 11, 14, 13, 16, 15, 18])
customer_satisfaction = np.array([80, 82, 83, 85, 87, 89, 90, 92, 95, 97, 98, 99])

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plotting the existing data series
ax1.plot(months, productivity_software, 'o-', label='Productivity Software', color='tab:blue')
ax1.plot(months, productivity_hardware, 's--', label='Productivity Hardware', color='tab:blue')

# Plotting the new data series
ax1.plot(months, sales_growth, 'x-.', label='Sales Growth', color='tab:green')
ax1.set_ylim(0, 100)
ax1.set_xticks(months)
ax1.set_ylabel('Measurement Units')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(months, hours_worked, 'd-.', label='Hours Worked', color='tab:red')
ax2.plot(months, customer_satisfaction, '^--', label='Customer Satisfaction', color='tab:orange')
ax2.set_ylim(30, 110)
ax2.set_ylabel('Hours & Satisfaction Score')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()