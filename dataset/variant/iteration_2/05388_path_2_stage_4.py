import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Average temperatures in Fahrenheit - data groups are shuffled while maintaining dimensional structure
ny_temps = [76, 75, 82, 80, 74, 77, 79, 81, 78, 82, 83]  # Manually shuffled
la_temps = [74, 76, 73, 78, 72, 75, 77, 80, 79, 81, 82]  # Manually shuffled
chi_temps = [71, 70, 78, 76, 72, 74, 77, 73, 75, 79, 80] # Manually shuffled
hou_temps = [86, 89, 88, 92, 84, 87, 91, 85, 90, 93, 94] # Manually shuffled
phx_temps = [102, 105, 110, 107, 100, 103, 108, 101, 106, 104, 109] # Manually shuffled

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, ny_temps, marker='o', color='teal', linewidth=2)
ax.plot(years, la_temps, marker='s', color='gold', linewidth=2)
ax.plot(years, chi_temps, marker='^', color='mediumvioletred', linewidth=2)
ax.plot(years, hou_temps, marker='d', color='darkorange', linewidth=2)
ax.plot(years, phx_temps, marker='p', color='navy', linewidth=2)

plt.tight_layout()
plt.show()