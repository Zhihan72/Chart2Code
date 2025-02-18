import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

companies = ['TechCorp', 'InnovInc', 'GTech', 'FWorks', 'NGen']
techcorp_revenue = np.array([50, 55, 60, 65, 75, 85])
innovinc_revenue = np.array([40, 48, 55, 62, 70, 80])
gtech_revenue = np.array([30, 35, 42, 50, 58, 68])
fworks_revenue = np.array([25, 28, 35, 45, 52, 65])
ngen_revenue = np.array([20, 25, 30, 35, 40, 50])

revenues = np.array([techcorp_revenue, innovinc_revenue, gtech_revenue, fworks_revenue, ngen_revenue])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i in range(len(companies)):
    if i == 0:
        ax1.bar(years, revenues[i], color=colors[i], label=companies[i])
    else:
        bottom = np.sum(revenues[:i], axis=0)
        ax1.bar(years, revenues[i], color=colors[i], bottom=bottom, label=companies[i])

ax1.set_title('Major Tech Revenues (2015-20)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Rev (Bn $)', fontsize=12)
ax1.set_xticks(years)
ax1.legend(title="Cos", loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, linestyle='--', alpha=0.6)

revenue_2020 = revenues[:, -1]
ax2.pie(revenue_2020, labels=companies, autopct='%1.1f%%', colors=colors, startangle=140, pctdistance=0.8)
ax2.set_title('Rev Share (2020)', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()