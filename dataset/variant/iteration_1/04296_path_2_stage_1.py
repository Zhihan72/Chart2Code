import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

company_names = ['TechCorp A', 'Innovation Inc', 'GlobalTech', 'FutureWorks', 'NexGen']
techcorp_a_revenue = np.array([50, 55, 60, 65, 75, 85])
innovation_inc_revenue = np.array([40, 48, 55, 62, 70, 80])
globaltech_revenue = np.array([30, 35, 42, 50, 58, 68])
futureworks_revenue = np.array([25, 28, 35, 45, 52, 65])
nexgen_revenue = np.array([20, 25, 30, 35, 40, 50])

revenues = np.array([techcorp_a_revenue, innovation_inc_revenue, globaltech_revenue, futureworks_revenue, nexgen_revenue])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# New set of colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i in range(len(company_names)):
    if i == 0:
        ax1.bar(years, revenues[i], color=colors[i], label=company_names[i])
    else:
        bottom = np.sum(revenues[:i], axis=0)
        ax1.bar(years, revenues[i], color=colors[i], bottom=bottom, label=company_names[i])

ax1.set_title('Revenue of Major Tech Companies (2015-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (Billions of $)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years)
ax1.legend(title="Companies", loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, which='major', linestyle='--', alpha=0.6)

revenue_2020 = revenues[:, -1]
ax2.pie(revenue_2020, labels=company_names, autopct='%1.1f%%', colors=colors, startangle=140, pctdistance=0.8)
ax2.set_title('Revenue Share of Major Tech Companies (2020)', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()