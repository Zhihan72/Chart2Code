import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Data is swapped or altered while maintaining structure
age_18_24 = np.array([20, 30, 50, 65, 75, 95, 85, 110, 105, 115, 130])
age_25_34 = np.array([32, 42, 57, 68, 82, 91, 115, 120, 145, 165, 180])
age_35_44 = np.array([15, 25, 35, 48, 58, 68, 78, 83, 92, 102, 106])
age_45_54 = np.array([6, 12, 17, 22, 29, 32, 38, 42, 47, 52, 56])
age_55_plus = np.array([2, 3, 4, 6, 8, 10, 13, 17, 19, 23, 26])

fig, ax = plt.subplots(figsize=(14, 8))
# Stacked area chart using the altered data
ax.stackplot(years, age_18_24, age_25_34, age_35_44, age_45_54, age_55_plus,
             labels=['18-24', '25-34', '35-44', '45-54', '55+'],
             colors=['#FFD700', '#ADFF2F', '#1E90FF', '#FF69B4', '#DAA520'], alpha=0.8)

ax.set_title("Annual Tech Involvement Across Various Age Groups (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Tech-Involved Individuals (Thousands)", fontsize=12)

ax.legend(loc='upper left', title='Age Groups', fontsize=10, frameon=False)
ax.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()