import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
city_zephyr = np.array([500, 550, 600, 650, 700])
city_aerios = np.array([400, 450, 470, 490, 520])
city_nimus = np.array([300, 350, 400, 450, 460])

fig, ax = plt.subplots(figsize=(12, 7))

# Changed marker styles and line styles
ax.plot(years, city_zephyr, marker='x', linestyle='--', color='skyblue', label='City Zephyr')
ax.plot(years, city_aerios, marker='d', linestyle='-.', color='olive', label='City Aerios')
ax.plot(years, city_nimus, marker='v', linestyle=':', color='coral', label='City Nimus')

# Adjust grid style
ax.set_xticks(years)
ax.grid(True, linestyle=':', color='gray', alpha=0.7)

# Changed the legend style
ax.legend(title='City Comparison', fontsize=10, loc='upper left')

plt.tight_layout()
plt.show()