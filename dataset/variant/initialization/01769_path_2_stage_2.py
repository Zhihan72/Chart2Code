import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

years = np.arange(2011, 2021)

credit_cards = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42]
digital_wallets = [10, 12, 14, 17, 20, 25, 30, 35, 40, 45]
bank_transfers = [25, 23, 22, 20, 18, 15, 15, 14, 13, 10]
cryptocurrencies = [5, 7, 8, 9, 10, 10, 7, 5, 3, 3]
mobile_banking = [0, 1, 2, 4, 6, 8, 10, 12, 15, 20]

cumulative_market_share = {
    'Credit': np.cumsum(credit_cards),
    'Wallets': np.cumsum(digital_wallets),
    'Transfers': np.cumsum(bank_transfers),
    'Crypto': np.cumsum(cryptocurrencies),
    'M-Bnk': np.cumsum(mobile_banking)
}

fig = plt.figure(figsize=(18, 8))

ax1 = fig.add_subplot(121, projection='3d')

methods = ['Credit', 'Wallets', 'Transfers', 'Crypto', 'M-Bnk']
data = [credit_cards, digital_wallets, bank_transfers, cryptocurrencies, mobile_banking]

xpos = np.repeat(np.arange(len(years)), len(methods))
ypos = np.tile(np.arange(len(methods)), len(years))
zpos = np.zeros_like(xpos)
dx = dy = 0.5
dz = np.hstack(data)
colors = ['royalblue', 'gold', 'seagreen', 'crimson', 'purple']

for i, color in enumerate(colors):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
              color=color, alpha=0.8, label=methods[i], zsort='average')

ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(methods)))
ax1.set_yticklabels(methods)
ax1.set_zlabel('Transact Volume (%)')
ax1.set_zlim(0, 100)
ax1.set_title('Digital Payment Evolution\n(2011-20)',
              fontsize=14, fontweight='bold', pad=20)
ax1.legend(loc='upper right', title='Pay Modes', fontsize=10)

ax2 = fig.add_subplot(122)

for method, values in cumulative_market_share.items():
    ax2.plot(years, values, marker='o', label=method)

ax2.set_title('Market Growth: Pay Methods', fontsize=14, fontweight='bold')
ax2.set_xlabel('Time Period')
ax2.set_ylabel('Accumulated Shares (%)')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.legend(title='Pay Modes', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()