import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_yields = np.array([2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.6, 3.8, 3.9, 4.0])

plt.figure(figsize=(12, 8))
plt.plot(
    years, 
    average_yields, 
    '-o', 
    color='gold', 
    markerfacecolor='forestgreen', 
    markersize=8,
    alpha=0.8
)

plt.grid(linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()