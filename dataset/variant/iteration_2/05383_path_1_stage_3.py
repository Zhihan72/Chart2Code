import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020])
north_america = np.array([50, 80, 120, 180, 250])
europe = np.array([40, 70, 110, 160, 220])
asia = np.array([20, 40, 80, 130, 200])
oceania = np.array([15, 35, 70, 100, 150])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, north_america, marker='o', linestyle='-', color='orange', linewidth=2)
ax.plot(years, europe, marker='s', linestyle='--', color='cyan', linewidth=2)
ax.plot(years, asia, marker='^', linestyle='-.', color='magenta', linewidth=2)
ax.plot(years, oceania, marker='d', linestyle=':', color='lime', linewidth=2)

ax.set_title('Global Vegetal Intake Boom (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Intake Volume (Kilotons)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 301, 50))

for year, na, eu, as_, oc in zip(years, north_america, europe, asia, oceania):
    ax.annotate(f'{na}', (year, na), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{eu}', (year, eu), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{as_}', (year, as_), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(f'{oc}', (year, oc), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.tight_layout()
plt.show()