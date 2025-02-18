import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

mobile_phones = [250, 300, 350, 380, 450, 500, 520, 530, 600, 650, 700]
tablets = [120, 130, 135, 140, 160, 170, 175, 190, 200, 220, 230]
laptops = [80, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160]
desktops = [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
years_shifted = np.arange(len(years))

ax.bar(years_shifted - bar_width, mobile_phones, width=bar_width, color='#1f77b4', alpha=0.8)
ax.bar(years_shifted, tablets, width=bar_width, color='#ff7f0e', alpha=0.8)
ax.bar(years_shifted + bar_width, laptops, width=bar_width, color='#2ca02c', alpha=0.8)
ax.bar(years_shifted + 2 * bar_width, desktops, width=bar_width, color='#d62728', alpha=0.8)

ax.set_title('Gadget Sales (2015-2025)', fontsize=14, fontweight='bold')
ax.set_ylabel('Units Sold', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(years_shifted)
ax.set_xticklabels(years)

plt.tight_layout()
plt.show()