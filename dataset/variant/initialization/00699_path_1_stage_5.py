import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

average_yields_A = np.array([2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.6, 3.8, 3.9, 4.0])
average_yields_B = np.array([2.3, 2.5, 2.6, 2.8, 2.9, 3.0, 3.2, 3.3, 3.5, 3.7, 3.9])
error_margins_A = np.array([0.2, 0.25, 0.3, 0.3, 0.35, 0.4, 0.35, 0.3, 0.25, 0.2, 0.2])
error_margins_B = np.array([0.15, 0.2, 0.25, 0.25, 0.3, 0.35, 0.3, 0.25, 0.2, 0.15, 0.15])

plt.figure(figsize=(12, 8))
plt.barh(
    years - 0.2, 
    average_yields_A, 
    xerr=error_margins_A, 
    height=0.4, 
    capsize=5, 
    color='skyblue', 
    ecolor='gray', 
    alpha=0.7
)
plt.barh(
    years + 0.2, 
    average_yields_B, 
    xerr=error_margins_B, 
    height=0.4, 
    capsize=5, 
    color='skyblue', 
    ecolor='gray', 
    alpha=0.7
)

plt.grid(linestyle=':', alpha=0.8, axis='y')

plt.tight_layout()
plt.show()