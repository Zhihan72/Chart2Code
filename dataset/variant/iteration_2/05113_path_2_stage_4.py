import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])

efficiency_model_A = np.array([34, 32, 30, 28, 26, 24, 22])
efficiency_model_B = np.array([36, 34, 33, 29, 27, 25, 23])

plt.figure(figsize=(14, 8))

plt.plot(years, efficiency_model_A, 'x--', label='Module A', color='orange')
plt.plot(years, efficiency_model_B, '^:', label='Technology B', color='red')

plt.title('EV Performance Evolution (2010-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Energy Usage (kWh per 100 miles)', fontsize=12)

plt.annotate('Emergence of new motors', 
             xy=(2016, 28), xytext=(2014, 34), 
             arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='purple')
plt.annotate('Breakthrough in cells', 
             xy=(2020, 24), xytext=(2018, 30), 
             arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='brown')

plt.grid(linestyle='-', alpha=0.8, color='lightgray')
plt.legend(loc='lower right', fontsize=12, shadow=True)

plt.tight_layout()
plt.show()