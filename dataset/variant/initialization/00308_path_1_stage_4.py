import matplotlib.pyplot as plt
import numpy as np

# Shortened exoplanet names for labels
exoplanets = [
    'X1', 'N2', 'T Nova', 'Zypher', 'Cosmo', 
    'Artemis', 'Elysium', 'Solaria', 'Arcadia', 'Veridian', 
    'Orion', 'Aether', 'Nebula 7', 'Pulsar 8', 'V5'
]

distances = np.array([
    4.2, 8.6, 15.3, 20.7, 22.5, 28.4, 30.1, 35.0, 38.7, 40.0, 
    25.0, 18.3, 33.1, 29.8, 26.7
])

fig, ax = plt.subplots(figsize=(10, 6))  # Reduced plot size
y_pos = np.arange(len(exoplanets))

ax.barh(y_pos, distances, color='skyblue')
ax.set_yticks(y_pos)
ax.set_yticklabels(exoplanets)
ax.invert_yaxis()

plt.tight_layout()
plt.show()