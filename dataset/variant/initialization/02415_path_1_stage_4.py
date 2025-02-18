import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Original data
languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

# New made-up data series
languages_spoken_new = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
satisfaction_level_new = np.array([3, 4, 5, 5, 6, 6, 7, 7, 8, 8])

# Combine original and new data
total_languages = np.concatenate([languages_spoken, languages_spoken_new])
total_satisfaction = np.concatenate([satisfaction_level, satisfaction_level_new])

# Calculate average satisfaction for the combined unique languages
unique_languages, indices = np.unique(total_languages, return_inverse=True)
avg_satisfaction = np.zeros_like(unique_languages, dtype=float)
for i in range(len(unique_languages)):
    avg_satisfaction[i] = total_satisfaction[indices == i].mean()

x_new = np.linspace(unique_languages.min(), unique_languages.max(), 300)
spline = make_interp_spline(unique_languages, avg_satisfaction, k=3)
y_smooth = spline(x_new)

plt.figure(figsize=(10, 6))
plt.scatter(languages_spoken, satisfaction_level, color='crimson', s=80, alpha=0.8, edgecolor='k')
plt.scatter(languages_spoken_new, satisfaction_level_new, color='mediumseagreen', s=80, alpha=0.8, edgecolor='k')
plt.plot(x_new, y_smooth, color='steelblue', linewidth=2)

plt.title('Languages vs. Satisfaction', fontsize=16, color='darkblue')
plt.xlabel('Languages', fontsize=12)
plt.ylabel('Satisfaction', fontsize=12)
plt.xticks(np.arange(1, 11, 1))
plt.yticks(np.arange(1, 11, 1))

plt.tight_layout()
plt.show()