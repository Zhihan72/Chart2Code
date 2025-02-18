import matplotlib.pyplot as plt

# Data for the bar chart
festival_names = ['Harvest Celebration', 'Music Gala', 'Gastronomy Highlights']
participants = [7000, 5000, 4500]
bar_colors = ['#FFC36C', '#A5D4A0', '#D4A5A5']

# Data for the pie chart
festival_labels = ['Music Gala', 'Art Marathon', 'Literature Encounters', 'Gastronomy Highlights', 'Reenactment Memories', 'Harvest Celebration']
festival_distribution = [25, 20, 15, 10, 20, 10]
festival_colors = ['#FFABAB', '#A5D4A0', '#FFC36C', '#D4A5A5', '#E7EFCF', '#92E4EB']
explode = (0, 0.1, 0, 0.1, 0, 0)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Sorted bar chart
bars = ax[0].bar(festival_names, participants, color=bar_colors, edgecolor='grey', hatch='/')
for bar in bars:
    yval = bar.get_height()
    ax[0].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=10)

ax[0].set_title("Top Festival Attendees", fontsize=14, fontweight='bold', pad=20)
ax[0].set_ylabel("Participants Count", fontsize=12)
ax[0].set_ylim(0, 8000)
ax[0].grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')

# Pie chart
wedges, texts, autotexts = ax[1].pie(
    festival_distribution, 
    labels=festival_labels, 
    colors=festival_colors, 
    explode=explode, 
    autopct='%1.1f%%', 
    startangle=180, 
    pctdistance=0.75, 
    wedgeprops=dict(edgecolor='grey', linewidth=0.5),
    shadow=False
)
plt.setp(autotexts, size=10, weight="bold", color='blue')
plt.setp(texts, size=10)

centre_circle = plt.Circle((0, 0), 0.60, fc='lightgrey')
fig.gca().add_artist(centre_circle)

ax[1].set_title("Festival Share in Regions", fontsize=14, fontweight='bold', pad=20)

fig.suptitle("Festivals Overview in Avecondale", fontsize=18, fontweight='bold')

plt.tight_layout(pad=2)
plt.show()