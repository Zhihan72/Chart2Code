import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

heating = [20, 22, 19, 21, 20, 23, 25]
lighting = [3, 3, 3, 3, 4, 5, 5]
appliances = [8, 7, 6, 7, 8, 10, 11]
entertainment = [5, 4, 5, 6, 7, 8, 10]

energy_stack = np.row_stack((heating, lighting, appliances, entertainment))

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(days, energy_stack,
             colors=['#FF5733', '#3357FF', '#FF33A1', '#FFC733'], alpha=0.8, 
             edgecolor='k', linewidth=0.5)

ax.grid(True, linestyle=':', alpha=0.8, color='grey')

plt.xticks(rotation=30, ha='right')

plt.tight_layout()

plt.show()