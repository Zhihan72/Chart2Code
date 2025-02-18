import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

unique_languages = np.unique(languages_spoken)
avg_satisfaction = [satisfaction_level[languages_spoken == lang].mean() for lang in unique_languages]
unique_languages = np.array(unique_languages)
avg_satisfaction = np.array(avg_satisfaction)

unique_levels, frequency = np.unique(satisfaction_level, return_counts=True)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

axes[0].barh(unique_languages, avg_satisfaction, color='dodgerblue', alpha=0.8)
axes[0].set_xlabel('Satisfaction Level', fontsize=12)
axes[0].set_ylabel('Languages Spoken', fontsize=12)
axes[0].set_xticks(np.arange(1, 11, 1))
axes[0].set_yticks(unique_languages)

axes[1].barh(unique_levels, frequency, color='seagreen', alpha=0.7)
axes[1].set_xlabel('Languages Spoken Frequency', fontsize=12)
axes[1].set_ylabel('Communication Satisfaction', fontsize=12)
axes[1].set_xticks(np.arange(0, max(frequency) + 1, 1))
axes[1].set_yticks(unique_levels)

plt.tight_layout()

plt.show()