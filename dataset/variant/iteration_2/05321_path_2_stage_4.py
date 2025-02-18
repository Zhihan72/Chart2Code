import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

heating = [20, 22, 19, 21, 20, 23, 25]
# cooling = [10, 12, 9, 11, 10, 8, 7]  # This group is removed
lighting = [3, 3, 3, 3, 4, 5, 5]
appliances = [8, 7, 6, 7, 8, 10, 11]
# entertainment = [5, 4, 5, 6, 7, 8, 10]  # This group is removed

# Update the energy_stack without the removed groups
energy_stack = np.row_stack((heating, lighting, appliances))

fig, ax = plt.subplots(figsize=(12, 8))

# Update colors to reflect the new number of groups
ax.stackplot(days, energy_stack,
             colors=['#FF5733', '#3357FF', '#F0FF33'], alpha=0.8)

ax.grid(True, linestyle='-.', alpha=0.7)

plt.xticks(rotation=30, ha='right')
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()