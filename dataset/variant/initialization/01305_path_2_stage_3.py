import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_adoption = [2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40]
wind_adoption = [10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30]
hydro_adoption = [30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36]
geothermal_adoption = [3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 17]

plt.figure(figsize=(12, 6))

plt.plot(years, solar_adoption, color='orange', linestyle='-', marker='D', linewidth=1.5)
plt.plot(years, wind_adoption, color='blue', linestyle=':', marker='x', linewidth=2)
plt.plot(years, hydro_adoption, color='green', linestyle='-', marker='h', linewidth=1)
plt.plot(years, geothermal_adoption, color='purple', linestyle='--', marker='o', linewidth=1.5)

plt.subplot().spines['top'].set_visible(False)
plt.subplot().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()