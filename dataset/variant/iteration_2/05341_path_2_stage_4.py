import matplotlib.pyplot as plt
import numpy as np

# Data
festival_distribution = [15, 25, 10, 20, 20, 10]
single_color = '#92E4EB'  # Consistent color for all elements
explode = (0, 0, 0.1, 0.1, 0, 0)
participants = [7000, 4500, 5000]

# Create the main plot
fig, ax = plt.subplots(2, 1, figsize=(8, 16))

# Main Pie chart with a consistent color
wedges, _, autotexts = ax[0].pie(
    festival_distribution,
    colors=[single_color] * len(festival_distribution),  # Use the same color for all pieces
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    shadow=True
)

plt.setp(autotexts, size=12, weight="bold", color='black')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Bar chart for Participants with a consistent color
bars = ax[1].bar(range(len(participants)), participants, color=single_color, edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width()/2, yval + 200, int(yval), ha='center', va='bottom', fontsize=12)

ax[1].set_ylim(0, 8000)

plt.tight_layout()
plt.show()