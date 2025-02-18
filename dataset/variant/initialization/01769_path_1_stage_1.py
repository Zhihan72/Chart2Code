import matplotlib.pyplot as plt
import numpy as np

# Years of analysis
years = np.arange(2011, 2021)

# Percentage data of digital payment adoption over the years
credit_cards = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42]
digital_wallets = [10, 12, 14, 17, 20, 25, 30, 35, 40, 45]
bank_transfers = [25, 23, 22, 20, 18, 15, 15, 14, 13, 10]
cryptocurrencies = [5, 7, 8, 9, 10, 10, 7, 5, 3, 3]

# Initialize the figure
fig = plt.figure(figsize=(18, 8))

# First subplot: Horizontal Bar Chart
ax1 = fig.add_subplot(121)

# Prepare data for horizontal bar chart
methods = ['Credit Cards', 'Digital Wallets', 'Bank Transfers', 'Cryptocurrencies']
data = [credit_cards, digital_wallets, bank_transfers, cryptocurrencies]
colors = ['royalblue', 'gold', 'seagreen', 'crimson']
bar_width = 0.2

for i, (method, color) in enumerate(zip(methods, colors)):
    ax1.barh(years - i * bar_width, data[i], color=color, height=bar_width, label=method, alpha=0.8)

ax1.set_yticks(years)
ax1.set_yticklabels(years)
ax1.invert_yaxis()  # Invert y-axis to have the earliest year at the top
ax1.set_xlabel('Percentage of Transactions (%)')
ax1.set_xlim(0, 100)
ax1.set_title('Adoption of Digital Payment Methods in E-commerce\n(2011-2020)',
              fontsize=14, fontweight='bold', pad=20)
ax1.legend(loc='lower right', title='Payment Methods', fontsize=10)

# Second subplot: Line Chart for Cumulative Market Share
cumulative_market_share = {
    'Credit Cards': np.cumsum(credit_cards),
    'Digital Wallets': np.cumsum(digital_wallets),
    'Bank Transfers': np.cumsum(bank_transfers),
    'Cryptocurrencies': np.cumsum(cryptocurrencies)
}

ax2 = fig.add_subplot(122)

for method, values in cumulative_market_share.items():
    ax2.plot(years, values, marker='o', label=method)

ax2.set_title('Cumulative Market Share of Payment Methods', fontsize=14, fontweight='bold')
ax2.set_xlabel('Years')
ax2.set_ylabel('Cumulative Market Share (%)')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.legend(title='Payment Methods', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()
plt.show()