import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1990, 2000, 2010])
north_america = np.array([50, 400, 8000])
europe = np.array([80, 600, 9000])
asia = np.array([20, 500, 20000])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(decades, north_america, marker='o', linestyle='-', color='#EF476F', linewidth=2)
ax.plot(decades, europe, marker='s', linestyle='--', color='#06D6A0', linewidth=2)
ax.plot(decades, asia, marker='^', linestyle='-.', color='#118AB2', linewidth=2)

# Randomly altered textual elements
ax.set_title('S*olar P#ower R-evolution\nR#ise of S*olar C^apacity (1990-2010)', fontsize=14, pad=20)
ax.set_xlabel('T!ime Period', fontsize=12)
ax.set_ylabel('Total Solar MW Installed', fontsize=12)

ax.set_xlim(1985, 2015)
ax.set_ylim(0, 22000)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 22001, 4000))

ax.annotate('N.A. Solar Boost', 
            xy=(2000, north_america[1]), 
            xytext=(1993, 10000), 
            arrowprops=dict(arrowstyle='->', color='black'), 
            fontsize=10)

ax.annotate('Renewable EU Target',
            xy=(2010, europe[2]),
            xytext=(2005, europe[2] + 2000),
            arrowprops=dict(arrowstyle='->', color='darkgreen'),
            fontsize=10,
            color='darkgreen')

ax.annotate('Asian Solar Explosion',
            xy=(2010, asia[2]),
            xytext=(2005, asia[2] - 5000),
            arrowprops=dict(arrowstyle='->', color='darkblue'),
            fontsize=10,
            color='darkblue')

plt.tight_layout()

plt.show()