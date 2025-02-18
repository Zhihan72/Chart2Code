import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)

podcast_data = {
    'Mystery': np.array([1, 3, 6, 9, 14, 16, 18, 20, 21]),
    'Science': np.array([2, 4, 5, 7, 10, 14, 18, 23, 29]),
    'Wellness': np.array([1, 2, 3, 5, 7, 9, 12, 15, 18]),
    'Humor': np.array([3, 4, 6, 8, 10, 13, 15, 17, 20]),
    'Technology': np.array([0, 1, 2, 3, 4, 6, 8, 12, 16]),
    'Fiction': np.array([0, 1, 2, 4, 6, 8, 10, 11, 13]),
}

values = np.array(list(podcast_data.values()))
cumulative_listeners = values.sum(axis=0)

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, values, labels=podcast_data.keys(), 
             colors=['#8b0000', '#ffa500', '#4682b4', '#32cd32', '#800080', '#d2691e'], alpha=0.7)

ax.plot(years, cumulative_listeners, color='navy', linewidth=2.0, linestyle='-.', marker='x', label='Aggregate Listeners')

ax.set_title('Podcast Trends Over Time', fontsize=16, fontweight='medium')
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Audience in Millions', fontsize=13)

ax.annotate(f'2023 Total: {cumulative_listeners[-1]}M', xy=(2023, cumulative_listeners[-1]), xytext=(2020, cumulative_listeners[-1] + 5),
            arrowprops=dict(facecolor='blue', arrowstyle='wedge'), fontsize=11, fontweight='normal', color='grey')

ax.legend(loc='upper right', frameon=True, framealpha=0.5, edgecolor='gray')
ax.grid(linewidth=0.6, linestyle=':', color='gray', alpha=0.7)

plt.tight_layout()
plt.show()