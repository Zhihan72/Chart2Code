import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

decades = ['90s', '00s', '10s', '20s']
solar = np.array([5, 20, 100, 250])
wind = np.array([10, 50, 200, 500])
hydroelectric = np.array([200, 250, 300, 350])
geothermal = np.array([15, 25, 40, 60])

data = np.vstack([solar, wind, hydroelectric, geothermal])
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

plt.figure(figsize=(14, 9))
plt.stackplot(decades, data, labels=['Solar', 'Wind', 'Hydro', 'Geo'], colors=colors, alpha=0.8)

plt.xlabel('Decades', fontsize=12)
plt.ylabel('Energy (TWh)', fontsize=12)
plt.title('Growth of Renewables\nby Decade', fontsize=16, fontweight='bold', pad=20)

plt.legend(title='Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(visible=True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

plt.yticks(np.arange(0, 601, 100))
plt.gca().yaxis.set_minor_locator(MultipleLocator(50))
plt.grid(which='minor', linestyle=':', linewidth=0.5)

plt.annotate('Solar Surge', xy=('10s', 100), xytext=('10s', 150),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='black')

plt.axvspan(2.5, 3.5, color='grey', alpha=0.1)

plt.tight_layout()
plt.show()