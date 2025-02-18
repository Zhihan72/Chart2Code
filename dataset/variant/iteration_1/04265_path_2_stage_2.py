import matplotlib.pyplot as plt
import numpy as np

# Data creation
years = np.arange(2010, 2020)

company_a_stock = [50, 55, 60, 58, 62, 65, 70, 75, 80, 85]
company_b_stock = [30, 33, 35, 38, 40, 45, 50, 55, 60, 65]

company_a_revenue = [200, 210, 220, 215, 230, 240, 260, 275, 290, 310]
company_b_revenue = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Swap the used axes
# Now ax1 will draw the bar chart
ax1.bar(np.arange(len(company_a_revenue)), company_a_revenue, width=0.4, color='orange', alpha=0.8, label='Company A Revenue')
ax1.bar(np.arange(len(company_a_revenue)) + 0.4, company_b_revenue, width=0.4, color='purple', alpha=0.8, label='Company B Revenue')

ax1.set_title('Annual Revenues (2010-2019)', fontsize=16, fontweight='normal')
ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Revenue (Million USD)', fontsize=13)
ax1.set_xticks(np.arange(len(company_a_revenue)) + 0.2)
ax1.set_xticklabels(years)
ax1.legend(loc='lower right', fontsize=11)
ax1.grid(True, linestyle='-', alpha=0.3, axis='y')

# ax2 will now draw the line chart
ax2.plot(years, company_a_stock, label='Company A Stock', color='orange', marker='v', linestyle='-.', linewidth=3)
ax2.plot(years, company_b_stock, label='Company B Stock', color='purple', marker='^', linestyle=':', linewidth=1)

ax2.set_title('Stock Prices (2010-2019)', fontsize=16, fontweight='normal')
ax2.set_xlabel('Year', fontsize=13)
ax2.set_ylabel('Stock Price (USD)', fontsize=13)
ax2.legend(loc='upper right', fontsize=11)
ax2.grid(True, linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()