import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
alpha_revenue = [1.2, 2.0, 3.4, 5.1, 6.7, 8.9, 10.5, 12.1, 14.3, 16.2, 17.8]
beta_revenue = [0.9, 1.4, 2.3, 3.1, 4.2, 5.4, 6.3, 7.8, 9.1, 10.4, 11.7]

alpha_employees = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
beta_employees = [15, 18, 20, 23, 26, 30, 33, 36, 40, 44, 47]

fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# Revenue Plot
ax[0].plot(years, alpha_revenue, label='AlphaTech', color='#2ca02c', marker='x')
ax[0].plot(years, beta_revenue, label='BetaWave', color='#d62728', marker='*')
ax[0].legend(loc='best', fontsize=11)
ax[0].grid(True, which='both', linestyle='-', linewidth=0.3, color='black', alpha=0.5)

# Employee Growth Plot
ax[1].plot(years, alpha_employees, label='AlphaTech', color='#2ca02c', linestyle='--', marker='x')
ax[1].plot(years, beta_employees, label='BetaWave', color='#d62728', linestyle='-', marker='*')
ax[1].legend(loc='lower left', fontsize=11)
ax[1].grid(False)

plt.tight_layout()
plt.show()