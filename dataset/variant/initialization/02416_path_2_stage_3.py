import numpy as np
import matplotlib.pyplot as plt

languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

unique_languages = np.unique(languages_spoken)
avg_satisfaction = [satisfaction_level[languages_spoken == lang].mean() for lang in unique_languages]

fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(unique_languages, avg_satisfaction, color='dodgerblue', alpha=0.8, edgecolor='k')
ax.set_yticks(np.arange(1, 11, 1))
ax.set_xticks(np.arange(1, 11, 1))
ax.grid(True, linestyle='--', alpha=0.7)

ax.set_xlabel('Average Satisfaction Level')
ax.set_ylabel('Languages Spoken')
plt.tight_layout()
plt.show()