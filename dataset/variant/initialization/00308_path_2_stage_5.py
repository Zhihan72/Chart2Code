import matplotlib.pyplot as plt
import numpy as np

exoplanets = ['Xeno 1', 'Nexus 2', 'Terra N.', 'Zypher', 'Cosmo P.',
              'Artemis', 'Elysium', 'Solaria', 'Arcadia', 'Veridian']
habitability_scores = np.array([0.8, 0.6, 0.9, 0.4, 0.5, 0.7, 0.3, 0.2, 0.6, 0.1])

# Shuffle the habitability_scores
shuffled_scores = np.array([0.5, 0.2, 0.9, 0.7, 0.1, 0.8, 0.4, 0.6, 0.3, 0.6])

plt.figure(figsize=(14, 7))
plt.bar(exoplanets, shuffled_scores, color='royalblue', alpha=0.85)

plt.title('Habitability Scores - Shuffled', fontsize=16, pad=20)
plt.xlabel('Exoplanet', fontsize=12)
plt.ylabel('Score', fontsize=12)

plt.tight_layout()
plt.show()