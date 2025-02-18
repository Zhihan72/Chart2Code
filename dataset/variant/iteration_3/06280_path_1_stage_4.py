import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(1980, 2020, 5))
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, country_a_production, marker='d', linestyle='--', linewidth=1.5, color='blue')

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()