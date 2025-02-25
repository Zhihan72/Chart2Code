import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2021)

car_commuters = np.array([50, 55, 58, 60, 62, 65, 66, 68, 70, 73, 75, 74, 73, 73, 74, 75])
public_transport_commuters = np.array([30, 32, 35, 37, 41, 45, 48, 52, 55, 57, 60, 63, 65, 68, 71, 74])
cycling_commuters = np.array([2, 3, 4, 5, 7, 9, 11, 14, 17, 19, 22, 25, 28, 30, 32, 35])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, car_commuters, public_transport_commuters, cycling_commuters,
             colors=['#fdae61', '#d73027', '#4575b4'], alpha=0.8,
             labels=['Car', 'Public Transport', 'Cycling'])

ax.set_xticks(years[::2])  # Change tick frequency for x-axis
ax.set_yticks(np.arange(0, 160, 20))  # Change tick frequency for y-axis

ax.grid(axis='both', linestyle='-.', alpha=0.5)  # Alter grid style and alpha

ax.spines['top'].set_visible(False)  # Remove top border
ax.spines['right'].set_linewidth(1.5)  # Change right border width

ax.legend(loc='upper left')  # Add a legend

plt.tight_layout()
plt.show()