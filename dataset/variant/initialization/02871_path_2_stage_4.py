import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2000, 10)

romance = np.array([25, 20, 25, 20, 22, 15, 10, 12, 18, 30])
war = np.array([15, 5, 8, 30, 10, 35, 15, 25, 5, 25])
identity = np.array([12, 35, 15, 18, 22, 10, 25, 40, 30, 42])
sci_fi = np.array([8, 1, 22, 4, 18, 25, 15, 12, 10, 2])

theme_data = np.vstack([romance, war, identity, sci_fi])

plt.figure(figsize=(14, 8))

# Shuffled colors
shuffled_colors = ['#8A2BE2', '#FF69B4', '#00CED1', '#FFA500']
line_styles = ['-', '--', '-.', ':']
marker_styles = ['^', 'v', 's', '*']

plt.stackplot(decades, theme_data, labels=['Rom.', 'War', 'Iden.', 'Sci-Fi'], colors=shuffled_colors, alpha=0.8)

plt.grid(visible=False)

plt.title('Themes in Lit. (1900-1999)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Prominence (%)', fontsize=12)

for i, theme in enumerate(theme_data):
    plt.plot(decades, np.cumsum(theme_data, axis=0)[i], linestyle=line_styles[i % len(line_styles)],
             marker=marker_styles[i % len(marker_styles)], markersize=6, color=shuffled_colors[i])
    for x, y in zip(decades, np.cumsum(theme_data, axis=0)[i]):
        plt.text(x, y, f'{y}%', fontsize=9, ha='center', va='bottom')

plt.xticks(decades, rotation=45)
plt.legend(loc='upper right', fontsize=10, title='Themes', title_fontsize='13')
plt.tight_layout()
plt.show()