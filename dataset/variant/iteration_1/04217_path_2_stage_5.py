import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

mobile_phones = [250, 300, 350, 380, 450, 500, 520, 530, 600, 650, 700]
laptops = [80, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160]
desktops = [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.2
years_shifted = np.arange(len(years))

ax.barh(years_shifted - bar_height, mobile_phones, height=bar_height, color='#5DADE2', alpha=0.8, label='Mobile Phones')
ax.barh(years_shifted, laptops, height=bar_height, color='#58D68D', alpha=0.8, label='Laptops')
ax.barh(years_shifted + bar_height, desktops, height=bar_height, color='#EB984E', alpha=0.8, label='Desktops')

ax.set_title('Gadget Sales (2015-2025)', fontsize=14, fontweight='bold')
ax.set_xlabel('Units Sold', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_yticks(years_shifted)
ax.set_yticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()