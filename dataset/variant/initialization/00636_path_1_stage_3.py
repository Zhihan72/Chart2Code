import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

parks = ["Central", "Riverside", "Brooklyn", "Liberty", "Queens BG"]

# Shuffled species_count and sightings manually
species_count = np.array([16, 18, 14, 15, 20])  # Changed from [15, 18, 14, 20, 16]
sightings = np.array([210, 240, 180, 200, 290])  # Changed from [200, 240, 180, 290, 210]

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

params, covariance = curve_fit(quadratic_model, species_count, sightings)

species_fit = np.linspace(min(species_count), max(species_count), 100)
sightings_fit = quadratic_model(species_fit, *params)

avg_sightings_per_species = sightings / species_count

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].scatter(species_count, sightings, color='darkgreen', label='Observed', s=100, alpha=0.7)
axes[0].plot(species_fit, sightings_fit, color='forestgreen', linestyle='--', label='Fit Curve', linewidth=2)
for i, park in enumerate(parks):
    axes[0].annotate(park, (species_count[i], sightings[i]), textcoords="offset points", xytext=(0, 10), ha='center')
axes[0].set_title("Birdwatching: Species vs. Sightings", fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel("Bird Species", fontsize=12)
axes[0].set_ylabel("Sightings", fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, frameon=True)
axes[0].grid(linestyle='--', alpha=0.5)

axes[1].barh(parks, avg_sightings_per_species, color='steelblue', alpha=0.7)
axes[1].set_title("Avg Sightings per Species", fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel("Avg Sightings", fontsize=12)
axes[1].set_ylabel("Parks", fontsize=12)
for i, v in enumerate(avg_sightings_per_species):
    axes[1].text(v + 0.2, i, f"{v:.1f}", color='black', va='center', fontweight='bold')

plt.tight_layout()
plt.show()