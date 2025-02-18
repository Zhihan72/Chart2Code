import matplotlib.pyplot as plt
import numpy as np

languages = ['Py', 'JS', 'Jv', 'C++', 'Rs']
python_scores = [9, 8, 7, 10, 9, 9, 8, 10, 8, 9]
javascript_scores = [8, 6, 7, 7, 8, 7, 6, 8, 8, 7]
java_scores = [6, 7, 6, 7, 6, 5, 6, 7, 7, 6]
cplusplus_scores = [5, 6, 6, 5, 5, 5, 4, 6, 6, 5]
rust_scores = [9, 9, 8, 9, 9, 8, 9, 9, 9, 8]
years = np.arange(2014, 2024)
avg_scores = {
    'Py': [9, 7, 8.5, 8, 8.7, 9, 9, 9.1, 9.3, 9.5],
    'JS': [7.9, 7.8, 7.4, 7, 6.5, 7.5, 6, 7.2, 7.5, 6],
    'Jv': [6.7, 6.8, 6.9, 5.5, 6.5, 6.8, 6, 6.5, 6.7, 6],
    'C++': [5, 4.5, 5, 5.7, 6, 5.8, 5.5, 5.2, 5.9, 5.7],
    'Rs': [9.7, 9.8, 8.8, 9.5, 9, 8.5, 9.2, 9.1, 9.3, 9.6]
}
language_scores = [python_scores, javascript_scores, java_scores, cplusplus_scores, rust_scores]
fig, axes = plt.subplots(2, 1, figsize=(8, 16))

box = axes[0].boxplot(language_scores, vert=False, patch_artist=True, labels=languages, notch=False, showfliers=True, whis=1.5)
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)
for whisker, cap, median in zip(box['whiskers'], box['caps'], box['medians']):
    whisker.set(color='#555555', linewidth=1.5)
    cap.set(color='#555555', linewidth=1.5)
    median.set(color='#e41a1c', linewidth=2)

axes[0].set_title('Lang Pop 2023', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Score')
axes[0].grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

for lang, color in zip(['Py', 'JS', 'Jv', 'C++', 'Rs'], colors):
    axes[1].plot(years, avg_scores[lang], marker='o', label=lang, color=color, linewidth=2, alpha=0.7)

axes[1].set_title('Trend by Year', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Yr')
axes[1].set_ylabel('Avg Score')
axes[1].grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(title='Lang', title_fontsize='10', fontsize='9', loc='upper left')

plt.tight_layout()
plt.show()