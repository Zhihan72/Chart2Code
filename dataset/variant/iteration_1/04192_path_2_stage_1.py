import matplotlib.pyplot as plt
import numpy as np

# Years in the decade span
years = np.arange(2010, 2021)

# Popularity scores (out of 100) for five different board games
settlers_of_catan = [60, 65, 68, 70, 75, 77, 76, 80, 83, 85, 88]
ticket_to_ride = [55, 58, 60, 63, 66, 70, 72, 75, 78, 80, 83]
pandemic = [45, 50, 55, 57, 60, 62, 65, 68, 70, 75, 78]
carcassonne = [50, 53, 55, 60, 63, 65, 70, 72, 74, 76, 79]
terraforming_mars = [10, 15, 20, 25, 30, 35, 40, 47, 55, 62, 70]

# Plotting the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Adding the lines for each board game
ax.plot(years, settlers_of_catan, label='CATAN', color='blue', linewidth=2)
ax.plot(years, ticket_to_ride, label='RIDE', color='orange', linewidth=2)
ax.plot(years, pandemic, label='DEMIC', color='green', linewidth=2)
ax.plot(years, carcassonne, label='CARCAS', color='red', linewidth=2)
ax.plot(years, terraforming_mars, label='MAR', color='purple', linewidth=2)

# Adding a subplot with bar chart to show the overall growth of board game popularity
board_games = ['CATAN', 'RIDE', 'DEMIC', 'CARCAS', 'MAR']
popularity_2010 = [60, 55, 45, 50, 10]
popularity_2020 = [88, 83, 78, 79, 70]
x = np.arange(len(board_games))  # Label locations
width = 0.35  # Width of the bars

ax_bar = ax.twinx()
ax_bar.barh(x - width/2, popularity_2010, width, label='2010 Status', color='skyblue', alpha=0.7)
ax_bar.barh(x + width/2, popularity_2020, width, label='2020 Status', color='navy', alpha=0.7)

# Customizing the main plot
ax.set_title("Trends of Board Games 2010-2020\nEvolution Overview", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Calendar Year", fontsize=14)
ax.set_ylabel("Score of Popularity", fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.legend(loc='upper left', fontsize=12, frameon=True)

# Customizing the subplot
ax_bar.set_yticks(x)
ax_bar.set_yticklabels(board_games, fontsize=12)
ax_bar.set_xlabel("Score Value", fontsize=14)
ax_bar.legend(loc='center right', fontsize=12, frameon=True)

# Adding a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()