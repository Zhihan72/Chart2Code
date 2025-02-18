import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

techcorp_stocks = [120, 135, 150, 180, 210, 250, 300, 350, 400, 450, 500]
innovateinc_stocks = [80, 85, 100, 140, 180, 220, 280, 330, 420, 520, 650]
futuresystems_stocks = [60, 70, 90, 110, 140, 170, 210, 260, 320, 400, 490]

plt.figure(figsize=(12, 8))

plt.plot(years, techcorp_stocks, color='blue', marker='s', linewidth=2, linestyle='-')
plt.plot(years, innovateinc_stocks, color='green', marker='d', linewidth=2, linestyle='--')
plt.plot(years, futuresystems_stocks, color='red', marker='o', linewidth=2, linestyle='-.')

plt.ylim(0, 700)

plt.tight_layout()

plt.show()