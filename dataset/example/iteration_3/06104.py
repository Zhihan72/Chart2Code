import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart shows the distribution of various energy sources used in a fictional futuristic city named NeoMetropolis. The pie chart visualizes the percentage share of different energy types, and the bar chart compares this data with the city plans for energy sources for the next decade.

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal']
current_share = [25, 20, 30, 15, 10]
future_share = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#00BFFF', '#32CD32', '#FFA07A', '#8A2BE2']
explode = (0.1, 0.05, 0.05, 0, 0.05)

# Creating a figure with 1 row and 2 columns for the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the pie chart
wedges, texts, autotexts = ax1.pie(current_share, labels=energy_sources, autopct='%1.1f%%', 
                                   startangle=140, colors=colors, explode=explode, shadow=True)

# Adding a donut hole
centre_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=1.25)
ax1.add_artist(centre_circle)

# Setting the title and adjusting label properties
ax1.set_title('Current Energy Source Distribution in NeoMetropolis', fontsize=14, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10)

# Custom legend outside the pie chart
ax1.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Bar chart to show future plans for energy sources
bar_width = 0.35
index = np.arange(len(energy_sources))

# Bars for current share and future share
rects1 = ax2.bar(index, current_share, bar_width, color=colors, label='Current Share', edgecolor='black')
rects2 = ax2.bar(index + bar_width, future_share, bar_width, color='#ADD8E6', label='Future Share', edgecolor='black')

# Title and labels
ax2.set_title('Projected Changes in Energy Source Distribution (Next Decade)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Energy Sources')
ax2.set_ylabel('Percentage Share')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(energy_sources)
ax2.legend()

# Adding values on top of the bars
def add_value_labels(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%', 
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_value_labels(ax2, rects1)
add_value_labels(ax2, rects2)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Display the plots
plt.show()