import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

credit_cards = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42]
digital_wallets = [10, 12, 14, 17, 20, 25, 30, 35, 40, 45]
bank_transfers = [25, 23, 22, 20, 18, 15, 15, 14, 13, 10]
cryptocurrencies = [5, 7, 8, 9, 10, 10, 7, 5, 3, 3]
mobile_banking = [0, 1, 2, 4, 6, 8, 10, 12, 15, 20]

sorted_credit_cards = sorted(credit_cards, reverse=True)
sorted_digital_wallets = sorted(digital_wallets, reverse=True)
sorted_bank_transfers = sorted(bank_transfers, reverse=True)
sorted_cryptocurrencies = sorted(cryptocurrencies, reverse=True)
sorted_mobile_banking = sorted(mobile_banking, reverse=True)

methods = ['Credit', 'Wallets', 'Transfers', 'Crypto', 'M-Bnk']
sorted_data = [sorted_credit_cards, sorted_digital_wallets, sorted_bank_transfers, sorted_cryptocurrencies, sorted_mobile_banking]

fig, ax = plt.subplots(figsize=(18, 8))

# Use a single color across all data groups
uniform_color = 'dodgerblue'

# Create sorted bar chart
for i, (method, data) in enumerate(zip(methods, sorted_data)):
    ax.bar(years + i * 0.15, data, color=uniform_color, width=0.15, label=method, alpha=0.6)

ax.set_xticks(years + 0.3)
ax.set_xticklabels(years)
ax.set_title('Sorted Digital Payment Evolution (2011-2020)', fontsize=12, fontweight='light')
ax.set_xlabel('Years')
ax.set_ylabel('Transaction Volume (%)')
ax.legend(title='Payment Modes', fontsize=9)

plt.tight_layout()
plt.show()