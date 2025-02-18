import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

unique_languages = np.unique(languages_spoken)
avg_satisfaction = [satisfaction_level[languages_spoken == lang].mean() for lang in unique_languages]
unique_languages = np.array(unique_languages)
avg_satisfaction = np.array(avg_satisfaction)

x_new = np.linspace(unique_languages.min(), unique_languages.max(), 300)
spline = make_interp_spline(unique_languages, avg_satisfaction, k=3)
y_smooth = spline(x_new)

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(unique_languages, avg_satisfaction, color='dodgerblue', s=80, alpha=0.8, edgecolor='k')
ax.plot(x_new, y_smooth, color='orange', linewidth=2)
ax.set_title('Impact of Multilingual Abilities on\nCommunication Satisfaction', fontsize=14, color='darkblue')
ax.set_xlabel('Number of Languages Spoken', fontsize=12)
ax.set_ylabel('Communication Satisfaction Level', fontsize=12)
ax.set_xticks(np.arange(1, 11, 1))
ax.set_yticks(np.arange(1, 11, 1))
ax.grid(True, linestyle='--', alpha=0.7)

highlight_points = [(2, 5), (5, 8), (9, 9)]
for (x, y) in highlight_points:
    ax.annotate(f'({x}, {y})', xy=(x, y), xytext=(-30, 10),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'),
                 fontsize=9, color='darkred')

plt.tight_layout()
plt.show()