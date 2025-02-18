import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

# Stock prices over 10 years for three companies
company_a_stock = [50, 55, 60, 58, 62, 65, 70, 75, 80, 85]
company_b_stock = [30, 33, 35, 38, 40, 45, 50, 55, 60, 65]
company_c_stock = [45, 48, 50, 51, 55, 58, 60, 62, 66, 70]

# Annual revenue (in millions) over 10 years for three companies
company_a_revenue = [200, 210, 220, 215, 230, 240, 260, 275, 290, 310]
company_b_revenue = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280]
company_c_revenue = [180, 190, 200, 210, 220, 230, 250, 270, 285, 300]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot stock prices with an additional series
ax1.plot(years, company_a_stock, label='Company A Stock Price', color='red', marker='^', linestyle='-.', linewidth=3)
ax1.plot(years, company_b_stock, label='Company B Stock Price', color='purple', marker='d', linestyle=':', linewidth=3)
ax1.plot(years, company_c_stock, label='Company C Stock Price', color='green', marker='o', linestyle='--', linewidth=3)

ax1.set_title('Stock Price Over Time\n(2010-2019)', fontsize=13, fontweight='normal')
ax1.set_xlabel('Year', fontsize=11)
ax1.set_ylabel('Stock Price (USD)', fontsize=11)
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, linestyle='-.', alpha=0.5)

# Adjust bar positions for three groups
bar_width = 0.25
bar_positions1 = np.arange(len(company_a_revenue))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width

# Plot revenue with an additional series
ax2.bar(bar_positions1, company_a_revenue, width=bar_width, color='orange', alpha=0.6, hatch='/', label='Company A Revenue')
ax2.bar(bar_positions2, company_b_revenue, width=bar_width, color='cyan', alpha=0.6, hatch='\\', label='Company B Revenue')
ax2.bar(bar_positions3, company_c_revenue, width=bar_width, color='lime', alpha=0.6, hatch='x', label='Company C Revenue')

ax2.set_title('Yearly Revenue\n(2010-2019)', fontsize=13, fontweight='normal')
ax2.set_xlabel('Year', fontsize=11)
ax2.set_ylabel('Revenue (Million USD)', fontsize=11)
ax2.set_xticks(bar_positions1 + bar_width)
ax2.set_xticklabels(years)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(False)

plt.tight_layout()
plt.show()