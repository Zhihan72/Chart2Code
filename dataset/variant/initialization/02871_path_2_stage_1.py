import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2000, 10)

# Original theme data for each decade
romance = np.array([30, 25, 20, 15, 10, 12, 18, 20, 22, 25])
war = np.array([5, 8, 15, 25, 30, 35, 25, 15, 10, 5])
identity = np.array([10, 12, 15, 18, 22, 25, 30, 35, 40, 42])
sci_fi = np.array([1, 2, 4, 8, 10, 12, 15, 18, 22, 25])

# Randomize data within themes while maintaining the original shape
romance = np.array([25, 20, 25, 20, 22, 15, 10, 12, 18, 30])
war = np.array([15, 5, 8, 30, 10, 35, 15, 25, 5, 25])
identity = np.array([12, 35, 15, 18, 22, 10, 25, 40, 30, 42])
sci_fi = np.array([8, 1, 22, 4, 18, 25, 15, 12, 10, 2])

# Stack the data
theme_data = np.vstack([romance, war, identity, sci_fi])

plt.figure(figsize=(14, 8))

colors = ['#FFB6C1', '#FFD700', '#87CEEB', '#8A2BE2']

plt.stackplot(decades, theme_data, labels=['Romance', 'War', 'Identity', 'Science Fiction'],
              colors=colors, alpha=0.8)

plt.grid(visible=True, color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

plt.title('Evolving Themes in Literature:\nA Century of Change (1900-1999)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Prominence in Literature (%)', fontsize=12)

for i, theme in enumerate(theme_data):
    plt.plot(decades, np.cumsum(theme_data, axis=0)[i], marker='o', markersize=5, color=colors[i])
    for x, y in zip(decades, np.cumsum(theme_data, axis=0)[i]):
        plt.text(x, y, f'{y}%', fontsize=9, ha='center', va='bottom')

plt.xticks(decades, rotation=45)
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.02, 1), title='Literary Themes', title_fontsize='13')
plt.tight_layout()
plt.show()