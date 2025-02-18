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
colors = ['seagreen', 'crimson', 'purple', 'gold', 'royalblue']  # Randomly shuffle color order

for i, color in enumerate(colors):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
              color=color, alpha=0.6, label=methods[i], zsort='min')  # Adjusted alpha and zsort

ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, rotation=30, ha='right')  # Adjusted rotation and text alignment
ax1.set_yticks(np.arange(len(methods)))
ax1.set_yticklabels(methods)
ax1.set_zlabel('Transaction Volume (%)')
ax1.set_zlim(0, 100)
ax1.set_title('Digital Payment Evolution\n(2011-2020)',
              fontsize=12, fontweight='light', pad=15)  # Changed font size and weight
ax1.legend(loc='lower left', title='Payment Modes', fontsize=8, frameon=False)  # Adjusted legend

ax2 = fig.add_subplot(122)

line_styles = ['-', '--', ':', '-.', '-']  # Different line styles
markers = ['v', '^', '<', '>', 's']  # Changed marker types
for method, (style, marker) in zip(cumulative_market_share.keys(), zip(line_styles, markers)):
    ax2.plot(years, cumulative_market_share[method], linestyle=style, marker=marker, label=method)

ax2.set_title('Market Growth by Payment Method', fontsize=12, fontweight='light')
ax2.set_xlabel('Years')
ax2.set_ylabel('Cumulative Share (%)')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=30, ha='right')
ax2.legend(title='Payment Modes', fontsize=9, shadow=True)  # Adjusted legend style
ax2.grid(False)  # Removed grid

plt.tight_layout()
plt.show()