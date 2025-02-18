import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar = np.array([3, 4, 5, 6, 8, 10, 12, 15, 18, 21, 24, 28, 32, 36, 40, 45, 50, 55, 60, 65, 70])
hydro = np.array([10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30])
nuclear = np.array([20, 18, 17, 16, 15, 14, 14, 13, 12, 12, 11, 10, 10, 10, 9, 8, 8, 7, 7, 6, 5])
fossil = 100 - (solar + hydro + nuclear)

fig, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(years, solar, hydro, nuclear, fossil, 
             colors=['#1f77b4', '#2ca02c', '#d62728', '#9467bd'], 
             alpha=0.85,
             labels=['Solar', 'Hydro', 'Nuclear', 'Fossil'])
ax.grid(False)
ax.legend(loc='upper left', fontsize=9, frameon=False)
ax.set_title('Energy Production Sources Over Time', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.spines['top'].set_linestyle('-.')
ax.spines['right'].set_linestyle('--')
plt.show()