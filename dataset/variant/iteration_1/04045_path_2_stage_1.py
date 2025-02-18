import matplotlib.pyplot as plt
import numpy as np

# Preparing the data
genres = ['Action', 'Role-Playing', 'Shooter', 'Sports', 'Puzzle']
market_share = [30, 25, 20, 15, 10]  # Market share percentages
new_colors = ['#FF6347', '#4682B4', '#D2691E', '#9ACD32', '#BA55D3']  # New colors associated with each genre

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=90,  # Starting angle for the first pie piece
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='white'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)  # Slightly explode each wedge
)

# Insert circle for 'donut' chart effect
centre_circle = plt.Circle((0,0), 0.75, fc='white')
fig.gca().add_artist(centre_circle)

# Title and legend
plt.title('Global Video Game Market Share by Genre in 2025', fontsize=16, fontweight='bold')
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Styling the text
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()