import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1010, 1020)

atlantis_festivals = np.array([[3, 2, 5, 4], [4, 6, 5, 3], [5, 3, 7, 5], [5, 4, 8, 6], [3, 5, 6, 4],
                               [4, 3, 5, 5], [4, 6, 6, 3], [5, 4, 7, 5], [6, 5, 5, 8], [6, 4, 9, 6]])
el_dorado_festivals = np.array([[4, 6, 1, 3], [5, 7, 4, 2], [6, 8, 4, 2], [5, 6, 3, 9], [4, 7, 2, 5],
                                [3, 4, 6, 4], [5, 7, 5, 2], [4, 6, 3, 8], [7, 4, 9, 4], [7, 4, 5, 10]])
shangri_la_festivals = np.array([[2, 4, 3, 5], [3, 4, 5, 6], [4, 6, 4, 6], [4, 5, 7, 7], [3, 5, 4, 6],
                                 [2, 4, 5, 6], [3, 5, 5, 7], [4, 5, 6, 6], [5, 6, 7, 6], [5, 5, 8, 7]])
avalon_festivals = np.array([[5, 4, 7, 6], [6, 5, 8, 7], [7, 5, 9, 7], [7, 6, 10, 8], [6, 5, 8, 7],
                             [5, 6, 7, 7], [6, 8, 8, 6], [7, 6, 9, 7], [8, 7, 7, 10], [8, 7, 6, 11]])

atlantis_diff = atlantis_festivals - np.mean(atlantis_festivals, axis=0)
el_dorado_diff = el_dorado_festivals - np.mean(el_dorado_festivals, axis=0)
shangri_la_diff = shangri_la_festivals - np.mean(shangri_la_festivals, axis=0)
avalon_diff = avalon_festivals - np.mean(avalon_festivals, axis=0)

colors = ['#FF6347', '#FFD700', '#8A2BE2', '#40E0D0']

fig, ax = plt.subplots(figsize=(14, 9))

for i, diff in enumerate([atlantis_diff, el_dorado_diff, shangri_la_diff, avalon_diff]):
    base = np.zeros(len(years))
    for j in range(diff.shape[1]):
        ax.bar(years, diff[:, j], bottom=base, color=colors[j], edgecolor='black')
        base += diff[:, j]

ax.set_title('Festivals Divergence in Mythical Places (1010-1019)', fontsize=14)
ax.set_ylabel('Festival Count Deviation from Avg')
ax.set_xlabel('Historical Year Span')
ax.set_xticks(years)

plt.show()