import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020])
north_america = np.array([50, 80, 120, 180, 250])
europe = np.array([40, 70, 110, 160, 220])
asia = np.array([20, 40, 80, 130, 200])
oceania = np.array([15, 35, 70, 100, 150])
south_america = np.array([30, 50, 90, 140, 190])
africa = np.array([10, 25, 55, 95, 140])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, north_america, marker='o', linestyle='-', color='orange', linewidth=2, label='North America')
ax.plot(years, europe, marker='s', linestyle='--', color='cyan', linewidth=2, label='Europe')
ax.plot(years, asia, marker='^', linestyle='-.', color='magenta', linewidth=2, label='Asia')
ax.plot(years, oceania, marker='d', linestyle=':', color='lime', linewidth=2, label='Oceania')
ax.plot(years, south_america, marker='p', linestyle='-', color='red', linewidth=2, label='South America')
ax.plot(years, africa, marker='h', linestyle='--', color='blue', linewidth=2, label='Africa')

ax.set_title('Global Vegetal Intake Boom (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Intake Volume (Kilotons)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 301, 50))

for year, na, eu, as_, oc, sa, af in zip(years, north_america, europe, asia, oceania, south_america, africa):
    ax.annotate(f'{na}', (year, na), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{eu}', (year, eu), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{as_}', (year, as_), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{oc}', (year, oc), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{sa}', (year, sa), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{af}', (year, af), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

ax.legend()
plt.tight_layout()
plt.show()