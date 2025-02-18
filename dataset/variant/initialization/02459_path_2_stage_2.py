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

# Altered textual elements
plt.errorbar(years, residential_speed, yerr=residential_variability, fmt='-o', color='teal', 
             capsize=5, alpha=0.8, label='Home Use', ecolor='lightgray')
plt.errorbar(years, business_speed, yerr=business_variability, fmt='-s', color='darkorange', 
             capsize=5, alpha=0.8, label='Commercial', ecolor='lightgray')
plt.errorbar(years, education_speed, yerr=education_variability, fmt='-d', color='forestgreen', 
             capsize=5, alpha=0.8, label='School Sector', ecolor='lightgray')
plt.errorbar(years, healthcare_speed, yerr=healthcare_variability, fmt='-^', color='crimson', 
             capsize=5, alpha=0.8, label='Health Services', ecolor='lightgray')

plt.title('Bandwidth Trends Over Time in Digital Metropolis\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Mean Bandwidth (Mbps)', fontsize=14)
plt.xticks(years, rotation=45)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Industry', fontsize=12, title_fontsize=14, loc='upper left')
plt.tight_layout()
plt.show()