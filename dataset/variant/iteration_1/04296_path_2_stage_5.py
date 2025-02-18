import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

companies = ['TechCorp', 'InnovInc', 'GTech', 'FWorks', 'NGen']
techcorp_revenue = np.array([52, 58, 63, 67, 78, 87])
innovinc_revenue = np.array([43, 49, 57, 65, 72, 82])
gtech_revenue = np.array([32, 37, 45, 48, 60, 70])
fworks_revenue = np.array([28, 29, 33, 47, 53, 66])
ngen_revenue = np.array([22, 27, 31, 33, 39, 52])

revenues_change = np.array([
    techcorp_revenue - techcorp_revenue[0],
    innovinc_revenue - innovinc_revenue[0],
    gtech_revenue - gtech_revenue[0],
    fworks_revenue - fworks_revenue[0],
    ngen_revenue - ngen_revenue[0]
])

fig, ax1 = plt.subplots(figsize=(14, 6))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i in range(len(companies)):
    if i == 0:
        ax1.bar(years, revenues_change[i], color=colors[i], label=companies[i])
    else:
        bottom = np.sum(revenues_change[:i], axis=0)
        ax1.bar(years, revenues_change[i], color=colors[i], bottom=bottom, label=companies[i])

ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_title('Major Tech Revenues Change (2015-20)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Change in Rev (Bn $)', fontsize=12)
ax1.set_xticks(years)
ax1.legend(title="Cos", loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()