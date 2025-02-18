import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)

podcast_data = {
    'Mystery': np.array([1, 3, 6, 9, 14, 16, 18, 20, 21]),
    'Science': np.array([2, 4, 5, 7, 10, 14, 18, 23, 29]),
    'Wellness': np.array([1, 2, 3, 5, 7, 9, 12, 15, 18]),
    'Humor': np.array([3, 4, 6, 8, 10, 13, 15, 17, 20]),
}

values = np.array(list(podcast_data.values()))
cumulative_listeners = values.sum(axis=0)

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, values, labels=podcast_data.keys(), colors=['#8b0000', '#ffa500', '#4682b4', '#32cd32'], alpha=0.8)

ax.plot(years, cumulative_listeners, color='black', linewidth=2.5, linestyle='--', marker='o', label='Aggregate Listeners')

ax.set_title('Podcast Trend Explosion (2015-2023):\nGrowth of Genre-Specific and Total Audience Patterns', fontsize=14, fontweight='bold')
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Audience Size (millions)', fontsize=12)

ax.annotate(f'Final Count: {cumulative_listeners[-1]}M', xy=(2023, cumulative_listeners[-1]), xytext=(2020, cumulative_listeners[-1] + 10),
            arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.5),
            fontsize=11, fontweight='bold', color='black')

ax.legend(loc='upper left', frameon=False)
ax.grid(linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()