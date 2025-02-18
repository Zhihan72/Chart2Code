import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

species_count = np.array([15, 18, 20, 16])
sightings = np.array([200, 240, 290, 210])

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

params, covariance = curve_fit(quadratic_model, species_count, sightings)
species_fit = np.linspace(min(species_count), max(species_count), 100)
sightings_fit = quadratic_model(species_fit, *params)
avg_sightings_per_species = sightings / species_count

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[1].scatter(species_count, sightings, color='purple', marker='x', s=80, alpha=0.6)
axes[1].plot(species_fit, sightings_fit, color='royalblue', linestyle='-', linewidth=2)
axes[1].grid(linestyle='-.', alpha=0.7)

axes[0].barh(range(len(avg_sightings_per_species)), avg_sightings_per_species, color='coral', alpha=0.8, edgecolor='black', hatch='//')
for i, v in enumerate(avg_sightings_per_species):
    axes[0].text(v + 0.5, i, f"{v:.1f}", color='blue', va='center', fontweight='bold')

plt.tight_layout()
plt.show()