import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1960, 2021)
co2_levels = [
    316, 317, 318, 319, 320, 321, 322, 323, 325, 326,
    327, 329, 330, 331, 332, 333, 335, 336, 337, 338,
    339, 340, 341, 342, 344, 345, 347, 348, 350, 351,
    353, 355, 356, 358, 359, 361, 363, 365, 367, 369,
    371, 373, 375, 377, 379, 381, 384, 386, 388, 390,
    392, 395, 397, 400, 403, 405, 407, 410, 412, 415,
    417
]

temperature_anomalies = [
    -0.02, 0.01, 0.03, 0.00, -0.05, 0.00, 0.05, 0.02, 0.01, 0.03,
    0.06, 0.04, 0.07, 0.10, 0.08, 0.09, 0.12, 0.10, 0.13, 0.15,
    0.14, 0.17, 0.15, 0.18, 0.19, 0.21, 0.20, 0.23, 0.22, 0.24,
    0.26, 0.25, 0.28, 0.27, 0.30, 0.33, 0.32, 0.35, 0.34, 0.38,
    0.37, 0.40, 0.39, 0.42, 0.41, 0.45, 0.43, 0.47, 0.46, 0.50,
    0.48, 0.52, 0.51, 0.55, 0.54, 0.58, 0.57, 0.61, 0.60, 0.64, 
    0.63
]

fig, ax = plt.subplots(figsize=(14, 8))

# New colors applied: 'darkorange' for CO2 levels and 'green' for temperature anomalies
ax.plot(years, co2_levels, color='darkorange', linestyle='-', marker='o', markersize=5, linewidth=2)
ax.plot(years, temperature_anomalies, color='green', linestyle='--', marker='s', markersize=5, linewidth=2)
ax.grid(True, linestyle='--', alpha=0.6)

ax.set_xticks(np.arange(1960, 2021, 5))
ax.set_yticks(np.arange(-0.1, 1.0, 0.1))

plt.tight_layout()
plt.show()