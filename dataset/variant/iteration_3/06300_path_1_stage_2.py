import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

industrial_solar = [5, 7, 9, 12, 15, 18, 20, 25, 28, 30, 32]
industrial_wind = [3, 4, 6, 8, 10, 12, 15, 17, 20, 22, 24]
industrial_hydro = [8, 10, 12, 15, 17, 19, 22, 24, 27, 30, 32]
industrial_geothermal = [2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]

residential_solar = [1, 3, 5, 8, 11, 14, 16, 19, 21, 23, 25]
residential_wind = [0.5, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
residential_hydro = [2, 3, 4, 6, 8, 10, 13, 15, 17, 19, 21]
residential_geothermal = [1, 2, 2, 3, 4, 5, 7, 8, 9, 10, 11]

transportation_solar = [1, 2, 2, 3, 4, 6, 7, 8, 10, 12, 14]
transportation_wind = [0.2, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8]
transportation_hydro = [0.8, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]
transportation_geothermal = [0.2, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

commercial_solar = [3, 5, 7, 9, 12, 14, 16, 18, 20, 22, 24]
commercial_wind = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
commercial_hydro = [1.5, 2, 3, 4, 6, 8, 10, 11, 13, 15, 18]
commercial_geothermal = [0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8]

plt.figure(figsize=(16, 14))

plt.subplot(4, 1, 1)
plt.stackplot(years, industrial_solar, industrial_wind, industrial_hydro, industrial_geothermal,
              colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(4, 1, 2)
plt.stackplot(years, residential_solar, residential_wind, residential_hydro, residential_geothermal,
              colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(4, 1, 3)
plt.stackplot(years, transportation_solar, transportation_wind, transportation_hydro, transportation_geothermal,
              colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(4, 1, 4)
plt.stackplot(years, commercial_solar, commercial_wind, commercial_hydro, commercial_geothermal,
              colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()