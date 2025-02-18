import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
productivity_software = np.array([73, 78, 80, 82, 85, 87, 86, 88, 90, 92, 94, 96])
productivity_hardware = np.array([65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 83, 85])
hours_worked = np.array([40, 42, 43, 45, 46, 47, 46, 48, 50, 52, 54, 55])
customer_satisfaction = np.array([80, 82, 81, 83, 84, 86, 85, 87, 89, 90, 91, 93])
employee_satisfaction = np.array([75, 76, 77, 78, 79, 81, 82, 83, 85, 86, 88, 89])

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.plot(months, productivity_software, 'o-', color='slateblue', label='Productivity Software')
ax1.plot(months, productivity_hardware, 's--', color='orangered', label='Productivity Hardware')
ax1.plot(months, customer_satisfaction, '^:', color='mediumseagreen', label='Customer Satisfaction')

ax1.set_ylim(60, 100)
ax1.set_xticks(months)
ax1.set_ylabel('Productivity and Satisfaction')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(months, hours_worked, 'd-.', color='seagreen', label='Hours Worked')
ax2.plot(months, employee_satisfaction, 'x-', color='gold', label='Employee Satisfaction')
ax2.set_ylim(35, 60)
ax2.set_ylabel('Hours and Satisfaction')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()