import matplotlib.pyplot as plt

fiction_scores = [7, 8, 8, 8, 9, 9, 9, 10, 6, 7, 8, 7, 9, 8, 8]
mystery_scores = [6, 7, 7, 8, 9, 8, 6, 7, 6, 7, 5, 8, 7, 6, 8]
science_fiction_scores = [5, 6, 7, 6, 5, 7, 8, 4, 9, 6, 5, 6, 4, 7, 6]
fantasy_scores = [9, 10, 8, 9, 8, 8, 9, 10, 10, 9, 8, 7, 9, 9, 8]
non_fiction_scores = [6, 7, 5, 6, 8, 5, 7, 6, 5, 7, 8, 6, 6, 5, 7]

genre_scores = [
    fiction_scores,
    mystery_scores,
    science_fiction_scores,
    fantasy_scores,
    non_fiction_scores
]

years = list(range(2013, 2024))
avg_scores = [
    [7.4, 7.8, 7.9, 8.0, 8.2, 8.1, 8.3, 8.5, 8.7, 8.0, 8.2],
    [6.3, 6.7, 7.0, 6.9, 7.1, 6.8, 7.0, 6.9, 7.3, 6.8, 7.0],
    [5.8, 6.0, 6.1, 6.3, 6.6, 6.8, 6.5, 6.4, 6.7, 6.5, 6.3],
    [9.1, 8.9, 9.0, 8.8, 9.2, 9.1, 9.3, 9.4, 9.2, 9.0, 9.1],
    [6.2, 6.3, 6.5, 6.4, 6.7, 6.5, 6.6, 6.4, 6.6, 6.4, 6.5]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(genre_scores, notch=False, patch_artist=True,
                 boxprops=dict(facecolor='lightcoral', color='crimson'),
                 whiskerprops=dict(color='crimson'),
                 capprops=dict(color='crimson'),
                 medianprops=dict(color='black'),
                 flierprops=dict(marker='x', markerfacecolor='darkorange', markersize=8, linestyle='none', markeredgecolor='forestgreen'))

colors = ['magenta', 'grey', 'cyan', 'lime', 'dodgerblue']
linestyles = ['-', '-.', ':', '--', '-']
for i, scores, color, linestyle in zip(range(1, 6), avg_scores, colors, linestyles):
    ax.plot([i - 0.2 + 0.4 * (j / (len(years) - 1)) for j in range(len(years))], scores, color=color, linestyle=linestyle, linewidth=2)

ax.set_xticks([])
ax.yaxis.grid(False)

ax.spines['top'].set_linestyle('--')
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linestyle('-')
ax.spines['right'].set_linewidth(2)

plt.show()