import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_18_24 = np.array([20, 30, 50, 65, 75, 95, 85, 110, 105, 115, 130])
age_25_34 = np.array([32, 42, 57, 68, 82, 91, 115, 120, 145, 165, 180])
age_35_44 = np.array([15, 25, 35, 48, 58, 68, 78, 83, 92, 102, 106])
age_45_54 = np.array([6, 12, 17, 22, 29, 32, 38, 42, 47, 52, 56])
age_55_plus = np.array([2, 3, 4, 6, 8, 10, 13, 17, 19, 23, 26])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, age_18_24, age_25_34, age_35_44, age_45_54, age_55_plus,
             colors=['#1E90FF', '#FFD700', '#DAA520', '#ADFF2F', '#FF69B4'], alpha=0.8)

# Removed textual elements
ax.legend(loc='upper right', fontsize=12, frameon=True, edgecolor='grey')
ax.grid(True, linestyle='-.', alpha=0.3, color='#777777')
ax.yaxis.set_major_locator(plt.MultipleLocator(20))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()