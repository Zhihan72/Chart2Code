import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Data: Renewable energy consumption in Terawatt-hours (TWh)
solar = [
    1.1, 1.4, 1.8, 2.3, 3.0, 3.8, 5.0, 6.2, 8.0, 10.1, 13.2, 17.0, 
    21.5, 27.0, 34.1, 39.6, 45.0, 52.2, 61.2, 71.3, 83.0
]
wind = [
    4.5, 5.2, 6.1, 7.4, 9.1, 11.0, 13.5, 16.5, 21.2, 26.0, 32.0, 
    38.8, 45.6, 53.2, 61.8, 70.0, 81.0, 94.0, 108.0, 120.0, 135.0
]
hydro = [
    50.0, 51.0, 52.0, 54.0, 55.0, 57.0, 59.5, 62.0, 65.0, 68.0, 71.0, 
    74.0, 77.0, 80.5, 84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 109.0
]
geothermal = [
    8.0, 8.5, 9.0, 9.2, 9.5, 9.8, 10.0, 10.5, 11.0, 11.5, 12.0, 
    12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar, marker='x', color='purple', linewidth=1.5, linestyle='--')
ax.plot(years, wind, marker='d', color='green', linewidth=1.5, linestyle=':')
ax.plot(years, hydro, marker='p', color='blue', linewidth=1.5, linestyle='-.')
ax.plot(years, geothermal, marker='o', color='orange', linewidth=1.5, linestyle='-')

ax.grid(True, linestyle='-', linewidth=0.3, alpha=0.9)

plt.tight_layout()
plt.show()