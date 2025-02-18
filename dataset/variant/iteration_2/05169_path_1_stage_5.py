import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)

# Data Arrays
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
ax[0].plot(years, alpha_revenue, color='#e41a1c', marker='o')  # Red
ax[0].plot(years, beta_revenue, color='#377eb8', marker='s')   # Blue
ax[0].plot(years, gamma_revenue, color='#4daf4a', marker='^')  # Green

# R&D Expenditure Plot
ax[1].plot(years, alpha_rd, color='#e41a1c', marker='o')  # Red
ax[1].plot(years, beta_rd, color='#377eb8', marker='s')   # Blue
ax[1].plot(years, gamma_rd, color='#4daf4a', marker='^')  # Green

# Employee Growth Plot
ax[2].plot(years, alpha_employees, color='#e41a1c', marker='o')  # Red
ax[2].plot(years, beta_employees, color='#377eb8', marker='s')   # Blue
ax[2].plot(years, gamma_employees, color='#4daf4a', marker='^')  # Green

# Remove borders
for axi in ax:
    axi.spines['top'].set_visible(False)
    axi.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()