import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

techcorp_stocks = [120, 135, 150, 180, 210, 250, 300, 350, 400, 450, 500]
innovateinc_stocks = [80, 85, 100, 140, 180, 220, 280, 330, 420, 520, 650]
futuresystems_stocks = [60, 70, 90, 110, 140, 170, 210, 260, 320, 400, 490]
futuretech_stocks = [50, 65, 80, 95, 130, 160, 200, 250, 310, 370, 450]

plt.figure(figsize=(12, 8))

# Randomly altering styles for each line
plt.plot(years, techcorp_stocks, label='TechC', color='blue', marker='x', linewidth=2, linestyle=':')
plt.plot(years, innovateinc_stocks, label='InnovInc', color='green', marker='v', linewidth=1.5, linestyle='-')
plt.plot(years, futuresystems_stocks, label='FutSys', color='red', marker='<', linewidth=3, linestyle='-.')
plt.plot(years, futuretech_stocks, label='FutTech', color='orange', marker='1', linewidth=2.5, linestyle='--')

# Annotating important points with altered style
for year, price in zip([2010, 2015, 2020], [120, 250, 500]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(5,-15), ha='right', fontsize=8, color='blue', backgroundcolor='yellow', alpha=0.5)
for year, price in zip([2010, 2015, 2020], [80, 220, 650]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-15,5), ha='left', fontsize=8, color='green', backgroundcolor='red', alpha=0.5)
for year, price in zip([2010, 2015, 2020], [60, 170, 490]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,-20), ha='center', fontsize=8, color='red', backgroundcolor='orange', alpha=0.6)
for year, price in zip([2010, 2015, 2020], [50, 160, 450]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(10,15), ha='center', fontsize=8, color='orange', backgroundcolor='blue', alpha=0.5)

plt.title('Tech Stocks (2010-20)', fontsize=20, fontweight='heavy')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Price (USD)', fontsize=12)
plt.ylim(0, 700)

# Altered grid style
plt.grid(True, linestyle='-', alpha=0.3)

# Randomly manipulating legend style
plt.legend(title='Companies', loc='lower right', fontsize=10, frameon=False)
plt.tight_layout()
plt.show()