import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)

# Manually shuffled data
alpha_revenue = [3.4, 6.7, 2.0, 5.1, 1.2, 8.9, 12.1, 16.2, 14.3, 10.5, 17.8]
beta_revenue = [4.2, 2.3, 3.1, 1.4, 9.1, 5.4, 7.8, 0.9, 6.3, 10.4, 11.7]
gamma_revenue = [7.2, 1.5, 11.3, 8.7, 5.6, 3.9, 2.6, 12.8, 16.0, 10.1, 14.5]

alpha_rd = [23, 18, 22, 17, 15, 21, 19, 25, 24, 20, 26]
beta_rd = [19, 12, 20, 16, 14, 18, 17, 19, 10, 13, 21]
gamma_rd = [26, 22, 1.5, 24, 20, 19, 21, 27, 23, 28, 25]

alpha_employees = [55, 35, 20, 25, 70, 45, 40, 30, 50, 65, 60]
beta_employees = [36, 26, 20, 23, 18, 33, 44, 30, 15, 40, 47]
gamma_employees = [35, 60, 45, 52, 41, 32, 38, 56, 28, 25, 49]

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Revenue Plot
ax[0].plot(years, alpha_revenue, label='AlphaTech', color='#1f77b4', marker='o')
ax[0].plot(years, beta_revenue, label='BetaWave', color='#ff7f0e', marker='s')
ax[0].plot(years, gamma_revenue, label='GammaSoft', color='#2ca02c', marker='^')
ax[0].set_title('Revenue Growth (2010-2020)', fontsize=14, fontweight='bold')
ax[0].set_ylabel('Revenue (in Billions)', fontsize=12)
ax[0].legend(loc='upper left', fontsize=10)
ax[0].grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# R&D Expenditure Plot
ax[1].plot(years, alpha_rd, label='AlphaTech', color='#1f77b4', marker='o')
ax[1].plot(years, beta_rd, label='BetaWave', color='#ff7f0e', marker='s')
ax[1].plot(years, gamma_rd, label='GammaSoft', color='#2ca02c', marker='^')
ax[1].set_title('R&D Expenditure as % of Revenue (2010-2020)', fontsize=14, fontweight='bold')
ax[1].set_ylabel('R&D Expenditure (%)', fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)
ax[1].grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Employee Growth Plot
ax[2].plot(years, alpha_employees, label='AlphaTech', color='#1f77b4', marker='o')
ax[2].plot(years, beta_employees, label='BetaWave', color='#ff7f0e', marker='s')
ax[2].plot(years, gamma_employees, label='GammaSoft', color='#2ca02c', marker='^')
ax[2].set_title('Employee Growth (2010-2020)', fontsize=14, fontweight='bold')
ax[2].set_xlabel('Year', fontsize=12)
ax[2].set_ylabel('Employees (in Thousands)', fontsize=12)
ax[2].legend(loc='upper left', fontsize=10)
ax[2].grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

plt.tight_layout()
plt.show()