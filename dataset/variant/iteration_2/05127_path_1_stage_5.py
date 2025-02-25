import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

glacier_a = np.array([3.0, 2.3, 2.8, 2.6, 2.1, 3.3, 2.4, 3.8, 3.2, 4.0, 3.6])
glacier_b = np.array([2.0, 3.2, 2.1, 1.9, 3.4, 1.8, 3.0, 2.7, 2.5, 2.8, 2.3])
glacier_c = np.array([2.9, 1.7, 2.4, 2.2, 1.5, 3.1, 1.6, 2.7, 2.5, 1.8, 2.0])

cumulative_a = np.cumsum(glacier_a)
cumulative_b = np.cumsum(glacier_b)
cumulative_c = np.cumsum(glacier_c)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Cumulative Loss Plot
axs[0].plot(years, cumulative_a, marker='v', label='Glacier A', color='#ff7f0e')
axs[0].plot(years, cumulative_b, marker='*', label='Glacier B', color='#2ca02c')
axs[0].plot(years, cumulative_c, marker='D', label='Glacier C', color='#d62728')

axs[0].set_title("Cumulative Loss (2012-22)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Cumul. Loss (Gt)", fontsize=12)
axs[0].legend(loc='upper left', title='Glaciers', fontsize=12)
axs[0].grid(True, linestyle=':', alpha=0.7)
axs[0].tick_params(axis='x', rotation=45)
axs[0].spines['top'].set_visible(False)

# Annual Ice Loss Plot
axs[1].plot(years, glacier_a, marker='v', label='Glacier A', color='#ff7f0e')
axs[1].plot(years, glacier_b, marker='*', label='Glacier B', color='#2ca02c')
axs[1].plot(years, glacier_c, marker='D', label='Glacier C', color='#d62728')

axs[1].set_title("Annual Ice Loss (2012-22)", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Loss (Gt/yr)", fontsize=12)
axs[1].legend(loc='upper left', title='Glaciers', fontsize=12)
axs[1].grid(True, linestyle=':', alpha=0.7)
axs[1].tick_params(axis='x', rotation=45)
axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()