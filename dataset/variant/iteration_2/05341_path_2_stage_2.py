import matplotlib.pyplot as plt
import numpy as np

# Main pie chart data: Festival types in Aveburrow
festival_labels = ['Art Festival', 'Harvest Festival', 'Historical Reenactment', 'Food Festival', 'Music Festival', 'Literature Festival']
festival_distribution = [15, 25, 10, 20, 20, 10]
festival_colors = ['#E7EFCF', '#FFABAB', '#A5D4A0', '#D4A5A5', '#FFC36C', '#92E4EB']
explode = (0, 0, 0.1, 0.1, 0, 0)

# Subplot data: Number of participants in the top festivals
festival_names = ['Music Festival', 'Food Festival', 'Harvest Festival']
participants = [7000, 4500, 5000]
bar_colors = ['#FFC36C', '#D4A5A5', '#FFABAB']

# Create the main plot
fig, ax = plt.subplots(2, 1, figsize=(8, 16))  # Changed from (1, 2) to (2, 1)

# Main Pie chart
wedges, texts, autotexts = ax[0].pie(
    festival_distribution, 
    labels=festival_labels, 
    colors=festival_colors, 
    explode=explode, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    shadow=True
)

plt.setp(autotexts, size=12, weight="bold", color='black')
plt.setp(texts, size=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax[0].set_title("Festival Distribution in Aveburrow", fontsize=16, fontweight='bold', pad=20)

# Subplot: Bar chart for Participants
bars = ax[1].bar(festival_names, participants, color=bar_colors, edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=12)

ax[1].set_title("Participants in Top Festivals", fontsize=16, fontweight='bold', pad=20)
ax[1].set_ylabel("Number of Participants")
ax[1].set_ylim(0, 8000)

fig.suptitle("Aveburrow Festivals Overview", fontsize=20, fontweight='bold',)

plt.tight_layout()
plt.show()