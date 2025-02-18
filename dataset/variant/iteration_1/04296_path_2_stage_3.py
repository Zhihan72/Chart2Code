import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

companies = ['TechCorp', 'InnovInc', 'GTech', 'FWorks', 'NGen']
techcorp_revenue = np.array([50, 55, 60, 65, 75, 85])
innovinc_revenue = np.array([40, 48, 55, 62, 70, 80])
gtech_revenue = np.array([30, 35, 42, 50, 58, 68])
fworks_revenue = np.array([25, 28, 35, 45, 52, 65])
ngen_revenue = np.array([20, 25, 30, 35, 40, 50])

# Calculate changes from the baseline (2015 revenues)
revenues_change = np.array([
    techcorp_revenue - techcorp_revenue[0],
    innovinc_revenue - innovinc_revenue[0],
    gtech_revenue - gtech_revenue[0],
    fworks_revenue - fworks_revenue[0],
    ngen_revenue - ngen_revenue[0]
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Diverging bar chart
for i in range(len(companies)):
    if i == 0:
        ax1.bar(years, revenues_change[i], color=colors[i], label=companies[i])
    else:
        bottom = np.sum(revenues_change[:i], axis=0)
        ax1.bar(years, revenues_change[i], color=colors[i], bottom=bottom, label=companies[i])

ax1.axhline(0, color='black', linewidth=0.8) # Central axis
ax1.set_title('Major Tech Revenues Change (2015-20)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Change in Rev (Bn $)', fontsize=12)
ax1.set_xticks(years)
ax1.legend(title="Cos", loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, linestyle='--', alpha=0.6)

revenue_2020 = revenues_change[:, -1]
ax2.pie(revenue_2020, labels=companies, autopct='%1.1f%%', colors=colors, startangle=140, pctdistance=0.8)
ax2.set_title('Rev Change Share (2020)', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()