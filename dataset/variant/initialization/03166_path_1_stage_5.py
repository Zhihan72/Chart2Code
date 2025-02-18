import matplotlib.pyplot as plt
import numpy as np

countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Denmark', 
             'Switzerland', 'Germany', 'Brazil', 'USA', 'Italy',
             'Spain', 'France', 'UK', 'Netherlands', 'Australia']
consumption = np.array([12.0, 10.5, 9.8, 9.0, 8.5, 7.9, 6.5, 5.0, 4.5, 4.0,
                        3.8, 3.6, 3.4, 3.2, 3.0])

sorted_indices = np.argsort(-consumption)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_consumption = consumption[sorted_indices]

new_colors = ['#4CAF50', '#FF5722', '#FFC107', '#2196F3', '#9C27B0', 
              '#00BCD4', '#E91E63', '#FFEB3B', '#8BC34A', '#009688',
              '#607D8B', '#795548', '#FF9800', '#F44336', '#3F51B5']

fig, ax = plt.subplots(figsize=(12, 12))
bars = ax.barh(sorted_countries, sorted_consumption, color=new_colors, height=0.6, edgecolor='grey', linestyle='-.')

for bar, value in zip(bars, sorted_consumption):
    ax.text(value + 0.2, bar.get_y() + bar.get_height() / 2, f'{value:.1f} kg', 
            va='center', fontsize=10, color='black', weight='bold')

ax.set_xlim(0, max(sorted_consumption) + 2)
ax.xaxis.grid(True, linestyle=':', color='lightgray', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()