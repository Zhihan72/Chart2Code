import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])

efficiency_model_A = np.array([34, 32, 30, 28, 26, 24, 22])
efficiency_model_B = np.array([36, 34, 33, 29, 27, 25, 23])

plt.figure(figsize=(14, 8))

plt.plot(years, efficiency_model_A, 'x--', label='EV Model A', color='orange')
plt.plot(years, efficiency_model_B, '^:', label='EV Model B', color='red')

plt.title('Progress in Electric Vehicle Efficiency (2010-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Efficiency (kWh/100 miles)', fontsize=12)

plt.annotate('Introduction of high-efficiency motors', 
             xy=(2016, 28), xytext=(2014, 34), 
             arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='purple')
plt.annotate('Advancement in battery technology', 
             xy=(2020, 24), xytext=(2018, 30), 
             arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='brown')

plt.grid(linestyle='-', alpha=0.8, color='lightgray')
plt.legend(loc='lower right', fontsize=12, shadow=True)

plt.tight_layout()
plt.show()