import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The fictional Town of Aveburrow is famous for its unique festivals. They celebrate a range of events throughout the year. 
# The pie chart will depict the distribution of different festivals celebrated in Aveburrow. Additionally, a subplot
# will illustrate the number of participants in some of the town’s most popular festivals.

# Main pie chart data: Festival types in Aveburrow
festival_labels = ['Harvest Festival', 'Music Festival', 'Art Festival', 'Literature Festival', 'Food Festival', 'Historical Reenactment']
festival_distribution = [25, 20, 15, 10, 20, 10]
festival_colors = ['#FFABAB', '#FFC36C', '#E7EFCF', '#92E4EB', '#D4A5A5', '#A5D4A0']
explode = (0, 0.1, 0, 0, 0.1, 0)

# Subplot data: Number of participants in the top festivals
festival_names = ['Harvest Festival', 'Music Festival', 'Food Festival']
participants = [5000, 7000, 4500]
bar_colors = ['#FFABAB', '#FFC36C', '#D4A5A5']

# Create the main plot
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

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

# Customize text and autotext properties
plt.setp(autotexts, size=12, weight="bold", color='black')
plt.setp(texts, size=12)

# Add a donut effect by drawing a circle at the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title for the main plot
ax[0].set_title("Festival Distribution in Aveburrow", fontsize=16, fontweight='bold', pad=20)

# Subplot: Bar chart for Participants
bars = ax[1].bar(festival_names, participants, color=bar_colors, edgecolor='black')

# Adding values on top of bars
for bar in bars:
    yval = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=12)

# Title and labels for subplot
ax[1].set_title("Participants in Top Festivals", fontsize=16, fontweight='bold', pad=20)
ax[1].set_ylabel("Number of Participants")
ax[1].set_ylim(0, 8000)

fig.suptitle("Aveburrow Festivals Overview", fontsize=20, fontweight='bold',)

# Adjust layout for both plots to fit
plt.tight_layout()
plt.show()