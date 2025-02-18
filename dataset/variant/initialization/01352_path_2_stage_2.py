import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

years = np.array(list(range(2010, 2025)))
ibm_quantum_volume = np.array([4, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768])
google_quantum_volume = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768])
rigetti_quantum_volume = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])
ionq_quantum_volume = np.array([0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

def exponential_growth(x, a, b):
    return a * np.exp(b * x)

params, _ = curve_fit(exponential_growth, years, ibm_quantum_volume, p0=[1, 0.1])

fig, ax = plt.subplots(figsize=(16, 10))

ax.plot(years, ibm_quantum_volume, marker='x', linestyle='--', color='#ff6347', linewidth=2)
ax.plot(years, google_quantum_volume, marker='v', linestyle='-', color='#4682b4', linewidth=2)
ax.plot(years, rigetti_quantum_volume, marker='s', linestyle=':', color='#8a2be2', linewidth=2)
ax.plot(years, ionq_quantum_volume, marker='p', linestyle='-.', color='#b8860b', linewidth=2)

ax.plot(years, exponential_growth(years, *params), linestyle='-', color='grey', linewidth=1.5)

ax.set_yscale('log')
ax.grid(False)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()