import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

# Manually shuffled data within parameters
glacier_a = np.array([3.0, 2.3, 2.8, 2.6, 2.1, 3.3, 2.4, 3.8, 3.2, 4.0, 3.6])
glacier_b = np.array([2.0, 3.2, 2.1, 1.9, 3.4, 1.8, 3.0, 2.7, 2.5, 2.8, 2.3])
glacier_c = np.array([2.9, 1.7, 2.4, 2.2, 1.5, 3.1, 1.6, 2.7, 2.5, 1.8, 2.0])

cumulative_a = np.cumsum(glacier_a)
cumulative_b = np.cumsum(glacier_b)
cumulative_c = np.cumsum(glacier_c)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Using the pre-shuffled data
axs[0].plot(years, cumulative_a, marker='o', label='A', color='#1f77b4')
axs[0].plot(years, cumulative_b, marker='s', label='B', color='#1f77b4')
axs[0].plot(years, cumulative_c, marker='^', label='C', color='#1f77b4')
axs[0].set_title("Cumulative Loss (2012-22)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Cumul. Loss (Gt)", fontsize=12)
axs[0].legend(title='Glaciers', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].tick_params(axis='x', rotation=45)

axs[1].plot(years, glacier_a, marker='o', label='A', color='#1f77b4')
axs[1].plot(years, glacier_b, marker='s', label='B', color='#1f77b4')
axs[1].plot(years, glacier_c, marker='^', label='C', color='#1f77b4')
axs[1].set_title("Annual Ice Loss (2012-22)", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Loss (Gt/yr)", fontsize=12)
axs[1].legend(title='Glaciers', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()