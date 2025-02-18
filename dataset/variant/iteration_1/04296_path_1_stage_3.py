import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

company_names = ['GlobalWorks', 'FutureGen', 'NexTech', 'InnoCorp', 'Tech Global']
# Manually shuffled revenue data for each company
globalworks_revenue = np.array([35, 28, 42, 30, 70, 65])
futuregen_revenue = np.array([52, 55, 30, 20, 48, 68])
nextech_revenue = np.array([60, 50, 25, 75, 65, 40])
innocorp_revenue = np.array([58, 68, 55, 62, 30, 85])
tech_global_revenue = np.array([40, 48, 35, 50, 52, 55])

revenues = np.array([globalworks_revenue, futuregen_revenue, nextech_revenue, innocorp_revenue, tech_global_revenue])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

colors = ['#66B3FF', '#FF6666', '#99FF99', '#FF9999', '#FFCC99']
markers = ['o', 's', '^', 'D', 'P']
line_styles = ['-', '--', '-.', ':', '-']

for i in range(len(company_names)):
    if i == 0:
        ax1.bar(years, revenues[i], color=colors[i], edgecolor='black', hatch='/', label=company_names[i])
    else:
        bottom = np.sum(revenues[:i], axis=0)
        ax1.bar(years, revenues[i], color=colors[i], edgecolor='black', hatch='/', bottom=bottom, 
                label=company_names[i])

ax1.set_title('Profits of Top Tech Enterprises (2015-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Timespan', fontsize=12)
ax1.set_ylabel('Profits (Billions $)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(title="Top Firms", loc='upper left', fontsize=10, frameon=True)
ax1.grid(True, which='major', linestyle='-', color='grey', alpha=0.3)

revenue_2020 = revenues[:, -1]
ax2.pie(revenue_2020, labels=company_names, autopct='%1.1f%%', colors=colors, startangle=140, pctdistance=0.85)
ax2.set_title('Market Share of Top Tech Firms (2020)', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()

plt.show()