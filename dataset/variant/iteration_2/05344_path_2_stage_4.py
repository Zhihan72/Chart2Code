import matplotlib.pyplot as plt
import numpy as np

# Calculate the average market share over the years for each company
solartech_share_avg = np.mean([20, 22, 24, 26, 27, 29, 31, 34, 36, 38, 40])
sunpower_share_avg = np.mean([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15])
firstsolar_share_avg = np.mean([15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 28])
others_share_avg = np.mean([40, 38, 36, 34, 33, 31, 29, 26, 23, 20, 17])

# Made-up data for EcoSun
ecosun_share_avg = np.mean([5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16])

# Updated market share values
market_share_avg = [solartech_share_avg, sunpower_share_avg, firstsolar_share_avg, others_share_avg, ecosun_share_avg]
labels = ['SolarTech', 'SunPower', 'First Solar', 'Others', 'EcoSun']
colors = ['#66b3ff', '#ffcc99', '#ff9999', '#99ff99', '#ff66cc']

fig, ax = plt.subplots(figsize=(8, 8))

# Create a donut pie chart
ax.pie(market_share_avg, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'))

ax.set_title("Average Solar Energy Market Share (2010-2020)", fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()