import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

parks = ["Central Park", "Riverside Park", "Liberty Park", "Queens Botanical Garden"]
species_count = np.array([15, 18, 20, 16])
sightings = np.array([200, 240, 290, 210])

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

params, covariance = curve_fit(quadratic_model, species_count, sightings)
species_fit = np.linspace(min(species_count), max(species_count), 100)
sightings_fit = quadratic_model(species_fit, *params)
avg_sightings_per_species = sightings / species_count

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].scatter(species_count, sightings, color='purple', marker='x', label='Observed Data', s=80, alpha=0.6)
axes[0].plot(species_fit, sightings_fit, color='royalblue', linestyle='-', label='Fitted Curve', linewidth=2)
for i, park in enumerate(parks):
    axes[0].annotate(park, (species_count[i], sightings[i]), textcoords="offset points", xytext=(5, 5), ha='right')
axes[0].set_title("Urban Birdwatching Trends:\nDiversity and Sightings in City Parks", fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel("Number of Bird Species", fontsize=12)
axes[0].set_ylabel("Total Sightings", fontsize=12)
axes[0].legend(loc='lower right', fontsize=10, frameon=False)
axes[0].grid(linestyle='-.', alpha=0.7)

axes[1].barh(parks, avg_sightings_per_species, color='coral', alpha=0.8, edgecolor='black', hatch='//')
axes[1].set_title("Average Sightings per Species\nin City Parks", fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel("Avg Sightings per Species", fontsize=12)
axes[1].set_ylabel("Parks", fontsize=12)
for i, v in enumerate(avg_sightings_per_species):
    axes[1].text(v + 0.5, i, f"{v:.1f}", color='blue', va='center', fontweight='bold')

plt.tight_layout()
plt.show()