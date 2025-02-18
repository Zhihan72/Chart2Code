import matplotlib.pyplot as plt
import numpy as np

langs = ['Py', 'JS', 'Java', 'C++', 'Rust']

py_scores = [8, 9, 8, 10, 9, 7, 9, 8, 9, 10]
js_scores = [7, 8, 6, 7, 8, 7, 6, 7, 8, 8]
java_scores = [6, 7, 6, 5, 6, 7, 6, 7, 7, 6]
cpp_scores = [5, 6, 5, 6, 5, 4, 5, 6, 6, 5]
rust_scores = [9, 8, 9, 9, 9, 9, 8, 9, 8, 9]

years = np.arange(2014, 2024)
avg_scores = {
    'Py': [7, 8, 8.5, 9, 8.7, 9, 9.2, 9.1, 9.3, 9.5],
    'JS': [6, 7, 6.5, 7.5, 7, 7.2, 7.5, 7.4, 7.8, 7.9],
    'Java': [5.5, 6, 6.5, 6, 6.5, 6.8, 6.7, 6.9, 6.8, 6.7],
    'C++': [4.5, 5, 5.2, 5.5, 5.7, 5.5, 5.8, 5.9, 5.7, 6],
    'Rust': [8.5, 8.8, 9, 9.2, 9.1, 9.5, 9.3, 9.6, 9.7, 9.8]
}

lang_scores = [py_scores, js_scores, java_scores, cpp_scores, rust_scores]

fig, axes = plt.subplots(2, 1, figsize=(10, 12))

box = axes[0].boxplot(lang_scores, vert=False, patch_artist=True, labels=langs, notch=False)
new_colors = ['#d95f02', '#1b9e77', '#7570b3', '#e7298a', '#66a61e']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)
for whisker, cap, median in zip(box['whiskers'], box['caps'], box['medians']):
    whisker.set(color='#555555', linewidth=1.5)
    cap.set(color='#555555', linewidth=1.5)
    median.set(color='#e41a1c', linewidth=2)

axes[0].set_title('Lang Popularity\n2023', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Score')
axes[0].set_yticklabels(langs)
axes[0].grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

for lang, color in zip(langs, new_colors):
    axes[1].plot(years, avg_scores[lang], marker='o', label=lang, color=color, linewidth=2, alpha=0.7)

axes[1].set_title('Yearly Trends', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Avg Score')
axes[1].grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(title='Langs', title_fontsize='10', fontsize='9', loc='upper left')

plt.tight_layout()
plt.show()