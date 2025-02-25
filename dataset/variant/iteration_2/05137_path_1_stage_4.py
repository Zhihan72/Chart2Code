import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar = np.array([5, 8, 15, 20, 30, 45, 60, 80, 100, 130, 170, 220, 280, 350, 430, 520, 620, 730, 850, 980, 1120])
wind = np.array([10, 15, 25, 35, 50, 70, 95, 120, 150, 185, 225, 270, 320, 375, 435, 500, 570, 645, 725, 810, 900])
hydro = np.array([20, 22, 25, 30, 35, 41, 48, 56, 65, 75, 86, 98, 111, 125, 140, 156, 173, 191, 210, 230, 251])
geothermal = np.array([1, 1.5, 2, 3, 4, 5.5, 7, 9, 11, 14, 17, 21, 25, 30, 35, 41, 47, 54, 61, 69, 77])

plt.figure(figsize=(20, 12))
plt.stackplot(years, solar, wind, hydro, geothermal, 
              colors=['#e69f00', '#56b4e9', '#009e73', '#0072b2'], alpha=0.8)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(20, 6))
solar_growth_rate = np.gradient(solar[:-1], years[:-1]) / solar[:-1] * 100
ax.plot(years[:-1], solar_growth_rate, color='#e69f00', linewidth=2.5)
plt.tight_layout()
plt.show()