import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
clay_yield = np.array([20, 22, 21, 24, 26, 25, 28])
loam_yield = np.array([30, 32, 33, 35, 36, 38, 40])
sandy_yield = np.array([15, 17, 16, 18, 20, 19, 21])
peaty_yield = np.array([25, 27, 26, 28, 29, 30, 31])

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(years, clay_yield, color='green', s=50, alpha=0.8, edgecolors='b', marker='x')
ax.scatter(years, loam_yield, color='yellow', s=80, alpha=0.6, edgecolors='g', marker='v')
ax.scatter(years, sandy_yield, color='purple', s=120, alpha=0.9, edgecolors='r', marker='P')
ax.scatter(years, peaty_yield, color='brown', s=70, alpha=0.5, edgecolors='y', marker='<')

clay_coefs = np.polyfit(years, clay_yield, 1)
loam_coefs = np.polyfit(years, loam_yield, 1)
sandy_coefs = np.polyfit(years, sandy_yield, 1)
peaty_coefs = np.polyfit(years, peaty_yield, 1)

ax.plot(years, np.poly1d(clay_coefs)(years), color='green', linestyle='-.')
ax.plot(years, np.poly1d(loam_coefs)(years), color='yellow', linestyle=':')
ax.plot(years, np.poly1d(sandy_coefs)(years), color='purple', linestyle='-')
ax.plot(years, np.poly1d(peaty_coefs)(years), color='brown', linestyle='-')

ax.grid(True, linestyle=':', alpha=0.4)

plt.tight_layout()
plt.show()