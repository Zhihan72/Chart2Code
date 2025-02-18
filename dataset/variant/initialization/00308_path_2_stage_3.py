import matplotlib.pyplot as plt
import numpy as np

# Exoplanet data
exoplanets = ['Xeno 1', 'Nexus 2', 'Terra Nova', 'Zypher', 'Cosmo Prime',
              'Artemis', 'Elysium', 'Solaria', 'Arcadia', 'Veridian']

# Habitability scores (on a scale of 0 to 1)
habitability_scores = np.array([0.8, 0.6, 0.9, 0.4, 0.5, 0.7, 0.3, 0.2, 0.6, 0.1])

# Sorting the exoplanets by habitability scores in descending order
sorted_indices = np.argsort(habitability_scores)[::-1]
sorted_exoplanets = [exoplanets[i] for i in sorted_indices]
sorted_scores = habitability_scores[sorted_indices]

# Create a bar chart
plt.figure(figsize=(14, 7))
plt.bar(sorted_exoplanets, sorted_scores, color='royalblue', alpha=0.85)

# Setting labels and title
plt.title('Exoplanet Habitability Scores', fontsize=16, pad=20)
plt.xlabel('Exoplanets', fontsize=12)
plt.ylabel('Habitability Score', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()