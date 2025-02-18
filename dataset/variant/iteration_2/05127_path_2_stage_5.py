import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

glacier_a = np.array([2.1, 2.3, 2.4, 2.6, 2.8, 3.0, 3.2, 3.3, 3.6, 3.8, 4.0])
glacier_b = np.array([1.8, 1.9, 2.0, 2.1, 2.3, 2.5, 2.7, 2.8, 3.0, 3.2, 3.4])
glacier_c = np.array([1.5, 1.6, 1.7, 1.8, 2.0, 2.2, 2.4, 2.5, 2.7, 2.9, 3.1])
glacier_d = np.array([1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.4, 2.5, 2.6, 2.8, 2.9])
glacier_e = np.array([2.0, 2.1, 2.2, 2.4, 2.6, 2.7, 2.8, 3.0, 3.1, 3.3, 3.5])

cumulative_a = np.cumsum(glacier_a)
cumulative_b = np.cumsum(glacier_b)
cumulative_c = np.cumsum(glacier_c)
cumulative_d = np.cumsum(glacier_d)
cumulative_e = np.cumsum(glacier_e)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Plot Cumulative Ice Loss now at the top
axs[0].plot(years, cumulative_a, marker='o', color='#1f77b4')
axs[0].plot(years, cumulative_b, marker='s', color='#ff7f0e')
axs[0].plot(years, cumulative_c, marker='^', color='#2ca02c')
axs[0].plot(years, cumulative_d, marker='*', color='#d62728')
axs[0].plot(years, cumulative_e, marker='x', color='#9467bd')
axs[0].set_title("Cumulative Ice Loss (2012-2022)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Cumulative Loss (Gt)", fontsize=12)
axs[0].tick_params(axis='x', rotation=45)

# Plot Annual Ice Loss now at the bottom
axs[1].plot(years, glacier_a, marker='o', color='#1f77b4')
axs[1].plot(years, glacier_b, marker='s', color='#ff7f0e')
axs[1].plot(years, glacier_c, marker='^', color='#2ca02c')
axs[1].plot(years, glacier_d, marker='*', color='#d62728')
axs[1].plot(years, glacier_e, marker='x', color='#9467bd')
axs[1].set_title("Annual Ice Loss (2012-2022)", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Loss (Gt/yr)", fontsize=12)
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()