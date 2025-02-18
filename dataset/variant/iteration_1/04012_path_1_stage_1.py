import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
city_zephyr = np.array([500, 550, 600, 650, 700])
city_aerios = np.array([400, 450, 470, 490, 520])
city_nimus = np.array([300, 350, 400, 450, 460])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, city_zephyr, marker='o', linestyle='-', color='skyblue', label='City Zephyr')
ax.plot(years, city_aerios, marker='s', linestyle='-', color='olive', label='City Aerios')
ax.plot(years, city_nimus, marker='^', linestyle='-', color='coral', label='City Nimus')

ax.set_xticks(years)
ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(title='City', fontsize=12)

plt.tight_layout()
plt.show()