import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
alpha_revenue = [1.2, 2.0, 3.4, 5.1, 6.7, 8.9, 10.5, 12.1, 14.3, 16.2, 17.8]
beta_revenue = [0.9, 1.4, 2.3, 3.1, 4.2, 5.4, 6.3, 7.8, 9.1, 10.4, 11.7]
gamma_revenue = [1.5, 2.6, 3.9, 5.6, 7.2, 8.7, 10.1, 11.3, 12.8, 14.5, 16.0]

alpha_rd = [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
beta_rd = [10, 12, 13, 14, 16, 17, 18, 19, 19, 20, 21]
gamma_rd = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

alpha_employees = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
beta_employees = [15, 18, 20, 23, 26, 30, 33, 36, 40, 44, 47]
gamma_employees = [25, 28, 32, 35, 38, 41, 45, 49, 52, 56, 60]

fig, ax = plt.subplots(3, 1, figsize=(12, 15))

# Revenue Plot
ax[0].plot(years, alpha_revenue, label='AlphaTech', color='#1f77b4', marker='x')
ax[0].plot(years, beta_revenue, label='BetaWave', color='#ff7f0e', marker='*')
ax[0].plot(years, gamma_revenue, label='GammaSoft', color='#2ca02c', marker='d')
ax[0].set_title('Revenue Growth (2010-2020)', fontsize=14, fontweight='bold')
ax[0].set_ylabel('Revenue (in Billions)', fontsize=12)
ax[0].legend(loc='best', fontsize=11)
ax[0].grid(True, which='both', linestyle='-', linewidth=0.3, color='black', alpha=0.5)

# R&D Expenditure Plot
ax[1].plot(years, alpha_rd, label='AlphaTech', color='#1f77b4', linestyle='-.', marker='x')
ax[1].plot(years, beta_rd, label='BetaWave', color='#ff7f0e', linestyle=':', marker='*')
ax[1].plot(years, gamma_rd, label='GammaSoft', color='#2ca02c', linestyle='-', marker='d')
ax[1].set_title('R&D Expenditure as % of Revenue (2010-2020)', fontsize=14, fontweight='bold')
ax[1].set_ylabel('R&D Expenditure (%)', fontsize=12)
ax[1].legend(loc='upper right', fontsize=11)
ax[1].grid(True, which='major', linestyle=':', linewidth=0.4, color='blue', alpha=0.6)

# Employee Growth Plot
ax[2].plot(years, alpha_employees, label='AlphaTech', color='#1f77b4', linestyle='--', marker='x')
ax[2].plot(years, beta_employees, label='BetaWave', color='#ff7f0e', linestyle='-', marker='*')
ax[2].plot(years, gamma_employees, label='GammaSoft', color='#2ca02c', linestyle='-', marker='d')
ax[2].set_title('Employee Growth (2010-2020)', fontsize=14, fontweight='bold')
ax[2].set_xlabel('Year', fontsize=12)
ax[2].set_ylabel('Employees (in Thousands)', fontsize=12)
ax[2].legend(loc='lower left', fontsize=11)
ax[2].grid(False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()