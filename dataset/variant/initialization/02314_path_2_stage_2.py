import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

sci_fi = np.array([14, 10, 12, 11, 13, 15])
mystery = np.array([10, 11, 8, 9, 10, 9])
fantasy = np.array([15, 12, 14, 16, 13, 13])
historical_fiction = np.array([9, 8, 10, 7, 9, 8])

errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
}

colors = ['#8c564b', '#1f77b4', '#2ca02c', '#ff7f0e']

fig, ax = plt.subplots(figsize=(12, 7))

ax.errorbar(years, sci_fi, yerr=errors["Sci-Fi"], label='Sci-Fi', color=colors[0], fmt='-o', capsize=5, alpha=0.8)
ax.errorbar(years, mystery, yerr=errors["Mystery"], label='Myst', color=colors[1], fmt='-s', capsize=5, alpha=0.8)
ax.errorbar(years, fantasy, yerr=errors["Fantasy"], label='Fant', color=colors[2], fmt='-^', capsize=5, alpha=0.8)
ax.errorbar(years, historical_fiction, yerr=errors["Historical Fiction"], label='Hist. Fic.', color=colors[3], fmt='-d', capsize=5, alpha=0.8)

ax.set_title("Lit Trends:\n2015-20", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Yr", fontsize=14)
ax.set_ylabel("Avg Books/Person", fontsize=14)
ax.set_xticks(years)
ax.legend(title='Genre', fontsize=12, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()