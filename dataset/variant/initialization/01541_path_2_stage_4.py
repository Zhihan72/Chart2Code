import matplotlib.pyplot as plt
import numpy as np

decades = ['90s', '00s', '10s', '20s']
solar = np.array([5, 20, 100, 250])
wind = np.array([10, 50, 200, 500])
hydroelectric = np.array([200, 250, 300, 350])
geothermal = np.array([15, 25, 40, 60])

data = np.vstack([solar, wind, hydroelectric, geothermal])
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

plt.figure(figsize=(14, 9))
plt.stackplot(decades, data, colors=colors, alpha=0.8)

plt.xlabel('Decades', fontsize=12)
plt.ylabel('Energy (TWh)', fontsize=12)
plt.title('Growth of Renewables\nby Decade', fontsize=16, fontweight='bold', pad=20)

plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, 601, 100))

plt.tight_layout()
plt.show()