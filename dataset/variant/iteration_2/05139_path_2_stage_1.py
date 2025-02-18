import numpy as np
import matplotlib.pyplot as plt

centuries = np.arange(1400, 2300, 200)
energy_flux = np.array([50, 70, 100, 130, 110, 90])
crystal_formation = np.array([10, 15, 25, 35, 32, 22])

fig, ax = plt.subplots(figsize=(14, 8))

ax.scatter(energy_flux, crystal_formation, color='purple', edgecolor='black', s=150, marker='*', alpha=0.7)

ax.set_title("Chronicles of Mystical Energy and Crystal Formation\n(1400 - 2200 AD)", fontsize=16, fontweight='bold')
ax.set_xlabel("Energy Flux (Mystical Index)", fontsize=14)
ax.set_ylabel("Crystal Formation Rate (per Century)", fontsize=14)

for i, century in enumerate(centuries):
    ax.annotate(f'{century} AD', (energy_flux[i], crystal_formation[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

fit = np.polyfit(energy_flux, crystal_formation, 1)
fit_fn = np.poly1d(fit)
ax.plot(energy_flux, fit_fn(energy_flux), color='blue', linestyle='--', linewidth=2)

ax.set_xticks(np.arange(40, 141, 20))
ax.set_yticks(np.arange(0, 41, 5))

plt.tight_layout()
plt.show()