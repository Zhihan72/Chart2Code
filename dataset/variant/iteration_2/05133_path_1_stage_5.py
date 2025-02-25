import matplotlib.pyplot as plt
import numpy as np

# Data
seasons = ["Blossom", "Heatwave", "Fallen Leaves", "Chill"]
drone_racing = [60, 70, 50, 80] 
robot_wrestling = [50, 40, 65, 60] 
ai_chess = [35, 50, 30, 45] 

# Combine seasons with the respective sport for sorting
drone_racing_combined = list(zip(drone_racing, seasons))
robot_wrestling_combined = list(zip(robot_wrestling, seasons))
ai_chess_combined = list(zip(ai_chess, seasons))

# Sort the combined lists (Descending order as an example)
drone_racing_combined.sort(reverse=True, key=lambda x: x[0])
robot_wrestling_combined.sort(reverse=True, key=lambda x: x[0])
ai_chess_combined.sort(reverse=True, key=lambda x: x[0])

# Separating sorted data and labels
drone_racing_sorted, seasons_dr = zip(*drone_racing_combined)
robot_wrestling_sorted, seasons_rw = zip(*robot_wrestling_combined)
ai_chess_sorted, seasons_ac = zip(*ai_chess_combined)

# Plotting bars
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each category in its own subplot position
br1 = np.arange(len(seasons))
ax.bar(br1, drone_racing_sorted, color='purple', edgecolor='grey')

# Set labels and title
ax.set_title('Nebula Sports Spectacle (Year 2125) - Sorted', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timelapses', fontsize=12)
ax.set_ylabel('Fans (Thousands)', fontsize=12)
ax.set_xticks(br1)
ax.set_xticklabels(seasons_dr)  # Sorted season labels for drone racing

# Annotations
for bar, ticket_sales in zip(ax.patches, drone_racing_sorted):
    height = bar.get_height()
    ax.annotate(f'{ticket_sales}k',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, color='black')

# Hide spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()