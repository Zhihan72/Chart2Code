import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

unique_languages, indices = np.unique(languages_spoken, return_inverse=True)
avg_satisfaction = np.zeros_like(unique_languages, dtype=float)
for i in range(len(unique_languages)):
    avg_satisfaction[i] = satisfaction_level[indices == i].mean()

x_new = np.linspace(unique_languages.min(), unique_languages.max(), 300)
spline = make_interp_spline(unique_languages, avg_satisfaction, k=3)
y_smooth = spline(x_new)

plt.figure(figsize=(10, 6))
plt.scatter(languages_spoken, satisfaction_level, color='dodgerblue', s=80, alpha=0.8, edgecolor='k')
plt.plot(x_new, y_smooth, color='orange', linewidth=2)

plt.xticks([])
plt.yticks([])
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()