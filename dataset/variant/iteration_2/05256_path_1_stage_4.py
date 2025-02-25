import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting Springfield Temperatures with random stylistic changes
ax.plot(months, springfield_temps, marker='x', linestyle='--', color='blue', label='Springfield')

# Plotting Laketown Temperatures with random stylistic changes
ax.plot(months, laketown_temps, marker='s', linestyle=':', color='red', label='Laketown')

# Enable grid with different style
ax.grid(True, linestyle='-', which='both', color='lightgrey', alpha=0.5)

# Adding a legend with a different location
ax.legend(loc='upper left', fontsize='medium', frameon=False)

# Tight layout and display the plot
plt.tight_layout()
plt.show()