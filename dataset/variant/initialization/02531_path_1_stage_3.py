import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2040)

planet_a_tourists = [20, 22, 27, 35, 40, 43, 45, 50, 56, 65]
planet_b_tourists = [15, 18, 21, 26, 30, 32, 37, 40, 44, 50]
planet_c_tourists = [10, 12, 15, 19, 23, 28, 31, 35, 38, 42]
planet_d_tourists = [8, 10, 12, 15, 20, 24, 27, 30, 33, 38]
planet_e_tourists = [5, 7, 10, 12, 16, 18, 21, 25, 28, 30]
planet_f_tourists = [12, 14, 18, 22, 26, 30, 33, 37, 41, 46]

planet_a_errors = [2, 2, 3, 3, 4, 3, 3, 4, 4, 5]
planet_b_errors = [1.5, 1.8, 2, 2.5, 3, 2.5, 3, 3.5, 3, 4]
planet_c_errors = [1, 1.2, 1.5, 1.8, 2, 2.8, 3, 3.2, 3.5, 4]
planet_d_errors = [0.8, 1, 1.2, 1.5, 1.8, 2.4, 2.7, 3, 3.3, 3.8]
planet_e_errors = [0.5, 0.7, 1, 1.2, 1.6, 1.8, 2.1, 2.5, 2.8, 3]
planet_f_errors = [1.2, 1.4, 1.6, 2, 2.4, 2.8, 3, 3.2, 3.5, 4]

fig, ax = plt.subplots(figsize=(12, 8))

ax.errorbar(years, planet_a_tourists, yerr=planet_a_errors, fmt='-o', capsize=5, color='#FF5733', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_b_tourists, yerr=planet_b_errors, fmt='-s', capsize=5, color='#33FFCE', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_c_tourists, yerr=planet_c_errors, fmt='-^', capsize=5, color='#335BFF', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_d_tourists, yerr=planet_d_errors, fmt='-D', capsize=5, color='#FF33A6', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_e_tourists, yerr=planet_e_errors, fmt='-p', capsize=5, color='#FFD700', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_f_tourists, yerr=planet_f_errors, fmt='-*', capsize=5, color='#7D3C98', linewidth=2, alpha=0.8)

ax.set_xticks(years)

plt.tight_layout()

plt.show()