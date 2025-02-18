import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal']
current_share = [25, 20, 30, 15, 10]
future_share = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#00BFFF', '#32CD32', '#FFA07A', '#8A2BE2']
explode = (0.1, 0.05, 0.05, 0, 0.05)

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 7))

bar_width = 0.35
index = np.arange(len(energy_sources))

# Converting the bar chart to a horizontal bar chart
rects1 = ax2.barh(index, current_share, bar_width, color=colors, label='Current Share', edgecolor='black')
rects2 = ax2.barh(index + bar_width, future_share, bar_width, color='#ADD8E6', label='Future Share', edgecolor='black')

ax2.set_title('Projected Changes in Energy Source Distribution (Next Decade)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Energy Sources')  # Change x-label to y-axis
ax2.set_xlabel('Percentage Share')  # Change y-label to x-axis
ax2.set_yticks(index + bar_width / 2)  # Use set_yticks for a horizontal bar
ax2.set_yticklabels(energy_sources)  # Use set_yticklabels for a horizontal bar
ax2.legend()

def add_value_labels(ax, rects):
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width}%', 
                    xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(3, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center')

add_value_labels(ax2, rects1)
add_value_labels(ax2, rects2)

wedges, texts, autotexts = ax1.pie(current_share, labels=energy_sources, autopct='%1.1f%%', 
                                   startangle=140, colors=colors, explode=explode, shadow=True)

centre_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=1.25)
ax1.add_artist(centre_circle)

ax1.set_title('Current Energy Source Distribution in NeoMetropolis', fontsize=14, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10)

ax1.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

plt.tight_layout()
plt.show()