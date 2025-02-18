import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2000, 10)

romance = np.array([30, 25, 20, 15, 10, 12, 18, 20, 22, 25])
war = np.array([5, 8, 15, 25, 30, 35, 25, 15, 10, 5])
sci_fi = np.array([1, 2, 4, 8, 10, 12, 15, 18, 22, 25])

theme_data = np.vstack([romance, war, sci_fi])

plt.figure(figsize=(14, 8))

colors = ['#4682B4', '#32CD32', '#DAA520']  # Changed colors

plt.stackplot(decades, theme_data, colors=colors, alpha=0.9)  # Altered alpha for opacity

plt.grid(visible=True, color='b', linestyle=':', linewidth=1, alpha=0.5)  # Random grid style

# Different marker shapes and line styles for each theme
markers = ['s--', 'x-', 'D-.']
for i, theme in enumerate(theme_data):
    plt.plot(decades, np.cumsum(theme_data, axis=0)[i], markers[i], markersize=7, color=colors[i])

plt.xticks(decades, rotation=45)

# Introduced border (spines) changes
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('grey')
plt.gca().spines['bottom'].set_color('grey')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.tight_layout()

plt.show()