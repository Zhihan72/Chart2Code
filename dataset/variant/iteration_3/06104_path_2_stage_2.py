import matplotlib.pyplot as plt
import numpy as np

# Updated data including experimental sources
energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal', 'Fusion', 'Biomass']
current_share = [25, 20, 30, 15, 10, 0, 0]
future_share = [35, 25, 20, 15, 5, 10, 5]
experimental_share = [5, 10, 5, 5, 5, 20, 20]

colors = ['#FFD700', '#00BFFF', '#32CD32', '#FFA07A', '#8A2BE2', '#FF4500', '#7FFF00']

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.25
index = np.arange(len(energy_sources))

rects1 = ax.bar(index, current_share, bar_width, color=colors, label='Current Share', edgecolor='black')
rects2 = ax.bar(index + bar_width, future_share, bar_width, color='#ADD8E6', label='Future Share', edgecolor='black')
rects3 = ax.bar(index + 2 * bar_width, experimental_share, bar_width, color='#FF6347', label='Experimental Share', edgecolor='black')

ax.set_title('Projected Changes in Energy Source Distribution (Next Decade)', fontsize=14, fontweight='bold')
ax.set_xlabel('Energy Sources')
ax.set_ylabel('Percentage Share')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(energy_sources)
ax.legend()

# Adding values on top of the bars
def add_value_labels(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%', 
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

add_value_labels(ax, rects1)
add_value_labels(ax, rects2)
add_value_labels(ax, rects3)

plt.tight_layout()
plt.show()