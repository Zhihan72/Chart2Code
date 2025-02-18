import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
population = np.array([
    152, 157, 159, 166, 172, 175, 182, 189, 199, 209,
    220, 236, 250, 259, 273, 286, 296, 311, 324, 339, 354
])
businesses = np.array([
    52, 54, 62, 67, 66, 70, 82, 88, 92, 102,
    109, 115, 130, 134, 141, 152, 156, 166, 178, 182, 194
])
household_income = np.array([
    34, 37, 39, 41, 41, 46, 49, 51, 54, 55,
    62, 61, 66, 72, 73, 79, 81, 87, 89, 95, 97
])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, population, color='red', linestyle='--', marker='D', linewidth=2, label='Population')
ax.plot(years, businesses, color='green', linestyle=':', marker='x', linewidth=2, label='Businesses')
ax.plot(years, household_income, color='blue', linestyle='-', marker='*', linewidth=2, label='Household Income')

ax.grid(False)

ax.set_xticks(np.arange(2000, 2021, 2))

milestones = [2005, 2010, 2015]
for year in milestones:
    ax.axvline(x=year, color='black', linestyle=':', linewidth=2.0, ymin=0.05, ymax=0.9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()