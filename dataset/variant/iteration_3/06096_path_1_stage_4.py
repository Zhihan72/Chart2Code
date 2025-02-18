import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_share = np.array([35, 20, 10, 50, 30, 45, 25, 40, 15])
revenue = np.array([5, 22, 1, 10, 3.5, 17, 2, 13.5, 7.5])
rnd_investment = np.array([1.8, 0.8, 5.5, 0.2, 7, 4, 0.5, 1.2, 2.5])
employee_growth = np.array([350, 50, 200, 110, 450, 150, 80, 60, 270])

fig, ax = plt.subplots(figsize=(14, 8))
ax.fill_between(years, market_share, color='mediumslateblue', alpha=0.6)
ax.fill_between(years, revenue, color='mediumseagreen', alpha=0.6)
ax.fill_between(years, rnd_investment, color='salmon', alpha=0.6)
ax.fill_between(years, employee_growth, color='gold', alpha=0.6)
plt.tight_layout()
plt.show()