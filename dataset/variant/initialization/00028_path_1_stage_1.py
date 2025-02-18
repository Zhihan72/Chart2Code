import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019])
solar_output = np.array([220, 245, 260, 280, 310])
wind_output = np.array([180, 210, 230, 270, 290])
hydro_output = np.array([260, 255, 265, 270, 275])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, solar_output, color='gold', marker='o', linewidth=2, linestyle='-')
ax.plot(years, wind_output, color='skyblue', marker='^', linewidth=2, linestyle='--')
ax.plot(years, hydro_output, color='blue', marker='s', linewidth=2, linestyle='-.')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Output (TWh)', fontsize=12)
ax.set_title('Annual Renewable Energy Output\nby Source (2015-2019)', fontsize=14)

plt.tight_layout()
plt.show()