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

# Randomly alter markers, line styles, and colors
ax.plot(years, ibm_quantum_volume, marker='x', linestyle='--', color='#ff6347', linewidth=2, label='IBM')
ax.plot(years, google_quantum_volume, marker='v', linestyle='-', color='#4682b4', linewidth=2, label='Google')
ax.plot(years, rigetti_quantum_volume, marker='s', linestyle=':', color='#8a2be2', linewidth=2, label='Rigetti')
ax.plot(years, ionq_quantum_volume, marker='p', linestyle='-.', color='#b8860b', linewidth=2, label='IonQ')

# Exponential fit line
ax.plot(years, exponential_growth(years, *params), linestyle='-', color='grey', linewidth=1.5, label='IBM Exponential Fit')

# Modify annotations
ax.annotate('IBM Quantum Milestone', xy=(2021, 512), xytext=(2015, 7000), arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, fontweight='bold')
ax.annotate('Google Achievement', xy=(2023, 4096), xytext=(2017, 20000), arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=9, fontweight='bold')

# Adjust labels for clarity
for i, year in enumerate(years):
    if i % 4 == 0:
        ax.text(year, ibm_quantum_volume[i], f'{ibm_quantum_volume[i]}', fontsize=8, ha='center')

# Modify title and axes
plt.title('Quantum Computing Power Over Time\nProjections by Company', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Quantum Volume', fontsize=12)
ax.set_yscale('log')
ax.grid(False)
ax.legend(title='Companies', loc='upper left', fontsize=9, frameon=True)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()