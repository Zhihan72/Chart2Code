import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

techcorp_stocks = [120, 135, 150, 180, 210, 250, 300, 350, 400, 450, 500]
innovateinc_stocks = [80, 85, 100, 140, 180, 220, 280, 330, 420, 520, 650]
futuresystems_stocks = [60, 70, 90, 110, 140, 170, 210, 260, 320, 400, 490]

plt.figure(figsize=(12, 8))

plt.plot(years, techcorp_stocks, label='TechC', color='purple', marker='s', linewidth=2, linestyle='-')
plt.plot(years, innovateinc_stocks, label='InnovInc', color='purple', marker='d', linewidth=2, linestyle='--')
plt.plot(years, futuresystems_stocks, label='FutSys', color='purple', marker='o', linewidth=2, linestyle='-.')

for year, price in zip([2010, 2015, 2020], [120, 250, 500]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='purple', backgroundcolor='white', alpha=0.8)
for year, price in zip([2010, 2015, 2020], [80, 220, 650]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='purple', backgroundcolor='white', alpha=0.8)
for year, price in zip([2010, 2015, 2020], [60, 170, 490]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='purple', backgroundcolor='white', alpha=0.8)

plt.title('Tech Stocks (2010-20)', fontsize=18, fontweight='bold')
plt.xlabel('Yr', fontsize=14)
plt.ylabel('Price (USD)', fontsize=14)
plt.ylim(0, 700)
plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(title='Cos', loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()