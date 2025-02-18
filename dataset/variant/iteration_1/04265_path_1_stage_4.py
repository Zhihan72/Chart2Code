import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

# Stock prices and revenue data for three companies
company_a_stock = [50, 55, 60, 58, 62, 65, 70, 75, 80, 85]
company_b_stock = [30, 33, 35, 38, 40, 45, 50, 55, 60, 65]
company_c_stock = [45, 48, 50, 51, 55, 58, 60, 62, 66, 70]

company_a_revenue = [200, 210, 220, 215, 230, 240, 260, 275, 290, 310]
company_b_revenue = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280]
company_c_revenue = [180, 190, 200, 210, 220, 230, 250, 270, 285, 300]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot stock prices with updated labels
ax1.plot(years, company_a_stock, label='A Stock', color='red', marker='^', linestyle='-.', linewidth=3)
ax1.plot(years, company_b_stock, label='B Stock', color='purple', marker='d', linestyle=':', linewidth=3)
ax1.plot(years, company_c_stock, label='C Stock', color='green', marker='o', linestyle='--', linewidth=3)

ax1.set_title('Stock Prices\n(2010-19)', fontsize=13)
ax1.set_xlabel('Year', fontsize=11)
ax1.set_ylabel('Price (USD)', fontsize=11)
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, linestyle='-.', alpha=0.5)

# Adjust bar positions for plots
bar_width = 0.25
bar_positions1 = np.arange(len(company_a_revenue))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width

# Plot revenue with adjusted labels
ax2.bar(bar_positions1, company_a_revenue, width=bar_width, color='orange', alpha=0.6, hatch='/', label='A Rev')
ax2.bar(bar_positions2, company_b_revenue, width=bar_width, color='cyan', alpha=0.6, hatch='\\', label='B Rev')
ax2.bar(bar_positions3, company_c_revenue, width=bar_width, color='lime', alpha=0.6, hatch='x', label='C Rev')

ax2.set_title('Revenue\n(2010-19)', fontsize=13)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_ylabel('Rev (M USD)', fontsize=11)
ax2.set_xticks(bar_positions1 + bar_width)
ax2.set_xticklabels(years)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(False)

plt.tight_layout()
plt.show()