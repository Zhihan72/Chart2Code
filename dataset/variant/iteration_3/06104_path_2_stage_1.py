import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal']
current_share = [25, 20, 30, 15, 10]
future_share = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#00BFFF', '#32CD32', '#FFA07A', '#8A2BE2']

# Creating a figure for the single subplot
fig, ax = plt.subplots(figsize=(7, 7))

# Bar chart to show future plans for energy sources
bar_width = 0.35
index = np.arange(len(energy_sources))

# Bars for current share and future share
rects1 = ax.bar(index, current_share, bar_width, color=colors, label='Current Share', edgecolor='black')
rects2 = ax.bar(index + bar_width, future_share, bar_width, color='#ADD8E6', label='Future Share', edgecolor='black')

# Title and labels
ax.set_title('Projected Changes in Energy Source Distribution (Next Decade)', fontsize=14, fontweight='bold')
ax.set_xlabel('Energy Sources')
ax.set_ylabel('Percentage Share')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(energy_sources)
ax.legend()

# Adding values on top of the bars
def add_value_labels(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%', 
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_value_labels(ax, rects1)
add_value_labels(ax, rects2)

plt.tight_layout()
plt.show()