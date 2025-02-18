import matplotlib.pyplot as plt
import numpy as np

# Data creation
years = np.arange(2010, 2020)

company_a_stock = [50, 55, 60, 58, 62, 65, 70, 75, 80, 85]

company_a_revenue = [200, 210, 220, 215, 230, 240, 260, 275, 290, 310]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Bar chart
ax1.bar(np.arange(len(company_a_revenue)), company_a_revenue, width=0.4, color='purple', alpha=0.8, label='Firm Alpha Earnings')

ax1.set_title('Fiscal Overview (2010-2019)', fontsize=16, fontweight='normal')
ax1.set_xlabel('Period', fontsize=13)
ax1.set_ylabel('Earnings (Million USD)', fontsize=13)
ax1.set_xticks(np.arange(len(company_a_revenue)))
ax1.set_xticklabels(years)
ax1.legend(loc='lower right', fontsize=11)
ax1.grid(True, linestyle='-', alpha=0.3, axis='y')

# Line chart
ax2.plot(years, company_a_stock, label='Firm Alpha Stock', color='purple', marker='v', linestyle='-.', linewidth=3)

ax2.set_title('Equity Price Trends (2010-2019)', fontsize=16, fontweight='normal')
ax2.set_xlabel('Temporal Marker', fontsize=13)
ax2.set_ylabel('Share Value (USD)', fontsize=13)
ax2.legend(loc='upper right', fontsize=11)
ax2.grid(True, linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()