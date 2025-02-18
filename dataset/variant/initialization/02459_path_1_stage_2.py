import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

residential_speed = np.array([4, 5, 6, 8, 10, 15, 20, 25, 35, 40, 45])
business_speed = np.array([10, 12, 15, 18, 24, 30, 35, 40, 50, 60, 70])
education_speed = np.array([6, 7, 9, 11, 14, 17, 22, 28, 34, 38, 42])

residential_variability = np.array([1, 1.2, 1.1, 1.5, 1.8, 2, 2.5, 3, 3.5, 4, 4.5])
business_variability = np.array([1.5, 1.6, 1.8, 2, 2.2, 2.4, 3, 3.5, 4, 4.5, 5])
education_variability = np.array([1.2, 1.3, 1.5, 1.7, 2, 2.2, 2.8, 3.2, 3.5, 4, 4.2])

plt.figure(figsize=(12, 8))

bar_width = 0.3

plt.barh(years - bar_width, residential_speed, xerr=residential_variability, height=bar_width, 
         align='center', color='navy', alpha=0.7, label='Residential Internet', ecolor='coral')
plt.barh(years, business_speed, xerr=business_variability, height=bar_width, 
         align='center', color='tomato', alpha=0.7, label='Business Net', ecolor='skyblue')
plt.barh(years + bar_width, education_speed, xerr=education_variability, height=bar_width, 
         align='center', color='purple', alpha=0.7, label='Education Connection', ecolor='gold')

plt.title('Cybercity Internet Speed Trends (2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Avg. Internet Speed (Mbps)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.xticks(np.arange(0, 81, 10))
plt.yticks(years)

plt.grid(True, linestyle='-.', alpha=0.5, axis='x')

plt.legend(title='Type of Connection', fontsize=12, title_fontsize=14, loc='upper right', borderpad=1)

plt.tight_layout()

plt.show()