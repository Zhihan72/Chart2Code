import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

# Stock prices over 10 years
company_a_stock = [50, 55, 60, 58, 62, 65, 70, 75, 80, 85]
company_b_stock = [30, 33, 35, 38, 40, 45, 50, 55, 60, 65]

# Annual revenue (in millions) over 10 years
company_a_revenue = [200, 210, 220, 215, 230, 240, 260, 275, 290, 310]
company_b_revenue = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280]

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot stock prices on the first subplot with shuffled colors
ax1.plot(years, company_a_stock, label='Company A Stock Price', color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, company_b_stock, label='Company B Stock Price', color='green', marker='s', linestyle='--', linewidth=2)

# Title and labels for the first subplot
ax1.set_title('Stock Price Evolution\n(2010-2019)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Stock Price (USD)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot revenue in the second subplot with shuffled colors
bar_width = 0.35
bar_positions1 = np.arange(len(company_a_revenue))
bar_positions2 = bar_positions1 + bar_width

ax2.bar(bar_positions1, company_a_revenue, width=bar_width, color='blue', alpha=0.7, label='Company A Revenue')
ax2.bar(bar_positions2, company_b_revenue, width=bar_width, color='green', alpha=0.7, label='Company B Revenue')

# Title and labels for the second subplot
ax2.set_title('Annual Revenue\n(2010-2019)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Revenue (Million USD)', fontsize=12)
ax2.set_xticks(bar_positions1 + bar_width / 2)
ax2.set_xticklabels(years)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()