import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

fig, ax = plt.subplots(figsize=(12, 8))

single_color = 'green'
ax.plot(months, springfield_temps, marker='o', linestyle='-', color=single_color)
ax.plot(months, laketown_temps, marker='o', linestyle='-.', color=single_color)

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()