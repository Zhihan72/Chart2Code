import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

ai_revenue = [6, 9, -15, 18, -9, 40]
cybersecurity_revenue = [15, -18, 20, -23, 25, 12]
blockchain_revenue = [1, -2, 3, -30, 30, -12]
cloud_revenue = [5, -8, 15, -22, 12, 50]

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(years, ai_revenue, color='#FF9999', align='center', linestyle='--')
ax.bar(years, cybersecurity_revenue, bottom=ai_revenue, color='#66B2FF', align='edge', linestyle='-')
new_bars = np.add(ai_revenue, cybersecurity_revenue).tolist()
ax.bar(years, blockchain_revenue, bottom=new_bars, color='#99FF99', align='center', linestyle='-.')
new_bars = np.add(new_bars, blockchain_revenue).tolist()
ax.bar(years, cloud_revenue, bottom=new_bars, color='#FFCC99', align='edge', linestyle=':')

ax.set_xticks(years)
ax.set_yticks(np.arange(-50, 51, 10))
ax.grid(True, linestyle='--', linewidth=0.5)
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()

plt.show()