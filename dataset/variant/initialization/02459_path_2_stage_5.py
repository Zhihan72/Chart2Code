import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Data for different sectors
residential_speed = np.array([4, 5, 6, 8, 10, 15, 20, 25, 35, 40, 45])
business_speed = np.array([10, 12, 15, 18, 24, 30, 35, 40, 50, 60, 70])
education_speed = np.array([6, 7, 9, 11, 14, 17, 22, 28, 34, 38, 42])
healthcare_speed = np.array([3, 4, 5, 7, 12, 14, 18, 23, 29, 35, 43])

residential_variability = np.array([1, 1.2, 1.1, 1.5, 1.8, 2, 2.5, 3, 3.5, 4, 4.5])
business_variability = np.array([1.5, 1.6, 1.8, 2, 2.2, 2.4, 3, 3.5, 4, 4.5, 5])
education_variability = np.array([1.2, 1.3, 1.5, 1.7, 2, 2.2, 2.8, 3.2, 3.5, 4, 4.2])
healthcare_variability = np.array([0.8, 1, 1.2, 1.4, 1.6, 1.9, 2.2, 2.5, 2.9, 3.1, 3.6])

plt.figure(figsize=(12, 8))

# Shuffle previously assigned colors manually
plt.barh(years - 0.3, residential_speed, xerr=residential_variability, 
         height=0.2, color='mediumvioletred', alpha=0.6, label='Home Usage', edgecolor='deepskyblue')
plt.barh(years - 0.1, business_speed, xerr=business_variability, 
         height=0.2, color='mediumseagreen', alpha=0.6, label='Corporate', edgecolor='deepskyblue')
plt.barh(years + 0.1, education_speed, xerr=education_variability, 
         height=0.2, color='teal', alpha=0.6, label='Educational', edgecolor='deepskyblue')
plt.barh(years + 0.3, healthcare_speed, xerr=healthcare_variability, 
         height=0.2, color='salmon', alpha=0.6, label='Health Sector', edgecolor='deepskyblue')

plt.title('Internet Speed Trends in Digital Metropolis\n(2010-2020)', fontsize=16, fontweight='bold')
plt.ylabel('Years', fontsize=12)
plt.xlabel('Average Bandwidth (Mbps)', fontsize=12)

plt.yticks(years)
plt.xticks(fontsize=10)

plt.grid(True, linestyle='-.', color='gray', alpha=0.3, axis='x')
plt.legend(title='Sectors', fontsize=10, title_fontsize=12, loc='best')
plt.tight_layout()
plt.show()