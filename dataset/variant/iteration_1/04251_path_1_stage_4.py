import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1990, 2000, 2010])
north_america = np.array([50, 400, 8000])
europe = np.array([80, 600, 9000])
asia = np.array([20, 500, 20000])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(decades, north_america, marker='o', linestyle='-', color='#FF5733', linewidth=2)
ax.plot(decades, europe, marker='s', linestyle='--', color='#33FF57', linewidth=2)
ax.plot(decades, asia, marker='^', linestyle='-.', color='#3357FF', linewidth=2)

ax.set_xlim(1985, 2015)
ax.set_ylim(0, 22000)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 22001, 4000))

plt.tight_layout()
plt.show()