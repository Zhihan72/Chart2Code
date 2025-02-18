import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([2.0, 4.1, 9.3, 13.4, 18.2, 22.3, 25.6, 25.3, 20.1, 14.0, 8.1, 3.2])
city_b_temps = np.array([-5.0, -2.8, 2.5, 10.1, 15.3, 19.8, 23.4, 22.9, 16.5, 9.0, 1.2, -3.7])

avg_city_a = np.mean(city_a_temps)
avg_city_b = np.mean(city_b_temps)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(months, city_a_temps, label='City Alpha', marker='x', color='#17becf', linestyle='-.', linewidth=2)
ax.plot(months, city_b_temps, label='City Beta', marker='d', color='#bcbd22', linestyle=':', linewidth=2)

ax.axhline(y=avg_city_a, color='#17becf', linestyle='-', linewidth=1.5, alpha=0.6)
ax.axhline(y=avg_city_b, color='#bcbd22', linestyle='-', linewidth=1.5, alpha=0.6)

ax.text(len(months)-1, avg_city_a, f'  Avg: {avg_city_a:.1f}°C', color='#17becf', verticalalignment='bottom')
ax.text(len(months)-1, avg_city_b, f'  Avg: {avg_city_b:.1f}°C', color='#bcbd22', verticalalignment='top')

ax.set_title('Monthly Avg Temperatures: City Alpha vs City Beta', fontsize=14, pad=15)
ax.set_xlabel('Months', fontsize=11)
ax.set_ylabel('Temperature (°C)', fontsize=11)

ax.annotate('Peak Summer', xy=('Jul', 25.6), xytext=('Jun', 27),
            arrowprops=dict(facecolor='#17becf', arrowstyle='|-|', lw=0.8),
            fontsize=9, color='#17becf')
ax.annotate('Winter Low', xy=('Jan', -5.0), xytext=('Feb', -12),
            arrowprops=dict(facecolor='#bcbd22', arrowstyle='fancy', lw=0.8),
            fontsize=9, color='#bcbd22')

ax.grid(visible=True, which='both', linestyle='-', linewidth=0.5, color='black', alpha=0.5)
ax.set_xticks(months)
ax.set_yticks(np.arange(-10, 31, 5))
ax.set_ylim(-12, 30)

ax.legend(title='City Names', title_fontsize='12', fontsize='9', loc='lower right')

plt.tight_layout()
plt.show()