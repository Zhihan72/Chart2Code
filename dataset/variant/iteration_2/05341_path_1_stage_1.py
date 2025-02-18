import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart: Festival types in Aveburrow
festival_labels = ['Harvest Festival', 'Music Festival', 'Art Festival', 'Literature Festival', 'Food Festival', 'Historical Reenactment']
festival_distribution = [25, 20, 15, 10, 20, 10]

# Shuffled colors for the pie chart
festival_colors = ['#A5D4A0', '#FFABAB', '#92E4EB', '#D4A5A5', '#E7EFCF', '#FFC36C']
explode = (0, 0.1, 0, 0, 0.1, 0)

# Data for the bar chart: Number of participants in the top festivals
festival_names = ['Harvest Festival', 'Music Festival', 'Food Festival']

# Shuffled colors for the bar chart
bar_colors = ['#D4A5A5', '#A5D4A0', '#FFC36C']
participants = [5000, 7000, 4500]

# Create the plots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart
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

# Customize text and autotext properties
plt.setp(autotexts, size=12, weight="bold", color='black')
plt.setp(texts, size=12)

# Add a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title for the pie chart
ax[0].set_title("Festival Distribution in Aveburrow", fontsize=16, fontweight='bold', pad=20)

# Bar chart for participants
bars = ax[1].bar(festival_names, participants, color=bar_colors, edgecolor='black')

# Add values on bars
for bar in bars:
    yval = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=12)

# Title and labels for bar chart
ax[1].set_title("Participants in Top Festivals", fontsize=16, fontweight='bold', pad=20)
ax[1].set_ylabel("Number of Participants")
ax[1].set_ylim(0, 8000)

fig.suptitle("Aveburrow Festivals Overview", fontsize=20, fontweight='bold',)

# Adjust layout
plt.tight_layout()
plt.show()