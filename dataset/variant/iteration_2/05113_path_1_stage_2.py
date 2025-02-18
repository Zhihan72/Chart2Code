import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])

efficiency_model_A = np.array([34, 32, 30, 28, 26, 24, 22])
efficiency_model_B = np.array([36, 34, 33, 29, 27, 25, 23])
efficiency_model_C = np.array([38, 36, 34, 33, 31, 29, 27])
efficiency_model_D = np.array([40, 37, 35, 32, 30, 28, 26])

plt.figure(figsize=(14, 8))
plt.plot(years, efficiency_model_A, '*-', label='EV Model A', color='red')
plt.plot(years, efficiency_model_B, '^--', label='EV Model B', color='cyan')
plt.plot(years, efficiency_model_C, 'h-.', label='EV Model C', color='magenta')
plt.plot(years, efficiency_model_D, 'p:', label='EV Model D', color='yellow')

plt.title('Progress in Electric Vehicle Efficiency (2010-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Efficiency (kWh/100 miles)', fontsize=12)

plt.annotate('Introduction of high-efficiency motors', 
             xy=(2016, 28), xytext=(2014, 32), 
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='blue')
plt.annotate('Advancement in battery technology', 
             xy=(2020, 24), xytext=(2018, 28), 
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='green')

plt.grid(linestyle='-', alpha=0.3)
plt.legend(loc='lower left', fontsize=10, frameon=True)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()