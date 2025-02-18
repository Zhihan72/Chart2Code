import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

residential_speed = np.array([4, 5, 6, 8, 10, 15, 20, 25, 35, 40, 45])
business_speed = np.array([10, 12, 15, 18, 24, 30, 35, 40, 50, 60, 70])
education_speed = np.array([6, 7, 9, 11, 14, 17, 22, 28, 34, 38, 42])
healthcare_speed = np.array([3, 4, 5, 7, 12, 14, 18, 23, 29, 35, 43])

residential_variability = np.array([1, 1.2, 1.1, 1.5, 1.8, 2, 2.5, 3, 3.5, 4, 4.5])
business_variability = np.array([1.5, 1.6, 1.8, 2, 2.2, 2.4, 3, 3.5, 4, 4.5, 5])
education_variability = np.array([1.2, 1.3, 1.5, 1.7, 2, 2.2, 2.8, 3.2, 3.5, 4, 4.2])
healthcare_variability = np.array([0.8, 1, 1.2, 1.4, 1.6, 1.9, 2.2, 2.5, 2.9, 3.1, 3.6])

plt.figure(figsize=(12, 8))

plt.errorbar(years, residential_speed, yerr=residential_variability, fmt=':_', color='teal', 
             capsize=7, alpha=0.6, label='Home Usage', ecolor='deepskyblue')
plt.errorbar(years, business_speed, yerr=business_variability, fmt='--v', color='salmon', 
             capsize=7, alpha=0.6, label='Corporate', ecolor='deepskyblue')
plt.errorbar(years, education_speed, yerr=education_variability, fmt='-.P', color='mediumseagreen', 
             capsize=7, alpha=0.6, label='Educational', ecolor='deepskyblue')
plt.errorbar(years, healthcare_speed, yerr=healthcare_variability, fmt='-*', color='mediumvioletred', 
             capsize=7, alpha=0.6, label='Health Sector', ecolor='deepskyblue')

plt.title('Internet Speed Trends in Digital Metropolis\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Average Bandwidth (Mbps)', fontsize=12)

plt.xticks(years, rotation=30)
plt.yticks(fontsize=10)

plt.grid(True, linestyle='-.', color='gray', alpha=0.3)
plt.legend(title='Sectors', fontsize=10, title_fontsize=12, loc='lower right')
plt.tight_layout()
plt.show()