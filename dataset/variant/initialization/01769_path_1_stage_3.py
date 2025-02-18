import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
credit_cards = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42]
digital_wallets = [10, 12, 14, 17, 20, 25, 30, 35, 40, 45]
bank_transfers = [25, 23, 22, 20, 18, 15, 15, 14, 13, 10]
cryptocurrencies = [5, 7, 8, 9, 10, 10, 7, 5, 3, 3]

fig = plt.figure(figsize=(18, 8))

# First subplot: Horizontal Bar Chart
ax1 = fig.add_subplot(121)

methods = ['Cards', 'Wallets', 'Bank', 'Crypto']
data = [credit_cards, digital_wallets, bank_transfers, cryptocurrencies]
colors = ['royalblue', 'gold', 'seagreen', 'crimson']
bar_width = 0.2

for i, (method, color) in enumerate(zip(methods, colors)):
    ax1.barh(years - i * bar_width, data[i], color=color, height=bar_width, alpha=0.8)

ax1.set_yticks(years)
ax1.invert_yaxis()
ax1.set_xlabel('% Transactions')
ax1.set_xlim(0, 100)

# Second subplot: Line Chart for Cumulative Market Share
cumulative_market_share = {
    'Cards': np.cumsum(credit_cards),
    'Wallets': np.cumsum(digital_wallets),
    'Bank': np.cumsum(bank_transfers),
    'Crypto': np.cumsum(cryptocurrencies)
}

ax2 = fig.add_subplot(122)

for method, values in cumulative_market_share.items():
    ax2.plot(years, values, marker='o')

ax2.set_xlabel('Year')
ax2.set_ylabel('Cumulative %')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')

plt.tight_layout()
plt.show()