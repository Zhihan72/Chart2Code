import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1990, 2000, 2010])
north_america = np.array([50, 400, 8000])
europe = np.array([80, 600, 9000])
asia = np.array([20, 500, 20000])

fig, ax = plt.subplots(figsize=(10, 6))

# Replacing the original colors with a new set
ax.plot(decades, north_america, marker='o', linestyle='-', color='#FF5733', linewidth=2)  # North America
ax.plot(decades, europe, marker='s', linestyle='--', color='#33FF57', linewidth=2)       # Europe
ax.plot(decades, asia, marker='^', linestyle='-.', color='#3357FF', linewidth=2)         # Asia

ax.set_title('Solar Power Revolution\nGrowth of Solar Capacity Installed by Region (1990-2010)', fontsize=14, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Installed Solar Capacity (MW)', fontsize=12)

ax.set_xlim(1985, 2015)
ax.set_ylim(0, 22000)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 22001, 4000))

ax.annotate('Major Solar Initiative', 
            xy=(2000, north_america[1]), 
            xytext=(1993, 10000), 
            arrowprops=dict(arrowstyle='->', color='black'), 
            fontsize=10)

ax.annotate('EU Renewable Directive',
            xy=(2010, europe[2]),
            xytext=(2005, europe[2] + 2000),
            arrowprops=dict(arrowstyle='->', color='darkgreen'),
            fontsize=10,
            color='darkgreen')

ax.annotate('Surge in Solar Installations',
            xy=(2010, asia[2]),
            xytext=(2005, asia[2] - 5000),
            arrowprops=dict(arrowstyle='->', color='darkblue'),
            fontsize=10,
            color='darkblue')

plt.tight_layout()

plt.show()