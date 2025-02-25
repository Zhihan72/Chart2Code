import matplotlib.pyplot as plt
import numpy as np

# Data: Ticket Sales in Thousands
seasons = ["Spring", "Summer", "Autumn", "Winter"]
drone_racing = [50, 80, 60, 70]
robot_wrestling = [40, 60, 50, 65]
ai_chess = [30, 45, 35, 50]
vr_gaming = [70, 75, 65, 80]

# Sort Data (Descending Order)
labels = np.array([seasons, drone_racing, robot_wrestling, ai_chess, vr_gaming])
sorted_indices = np.argsort([-x for x in drone_racing])  # Sorting by Drone Racing sales, descending

sorted_labels = labels[:, sorted_indices]

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot sorted Bar Chart
bar_width = 0.20
x = np.arange(len(seasons))  
br1 = x
br2 = [i + bar_width for i in br1]  
br3 = [i + bar_width for i in br2]  
br4 = [i + bar_width for i in br3]  

ax.bar(br1, sorted_labels[1].astype(int), color='orange', width=bar_width, edgecolor='grey', label='Drone Racing')
ax.bar(br2, sorted_labels[2].astype(int), color='blue', width=bar_width, edgecolor='grey', label='Robot Wrestling')
ax.bar(br3, sorted_labels[3].astype(int), color='green', width=bar_width, edgecolor='grey', label='AI Chess')
ax.bar(br4, sorted_labels[4].astype(int), color='purple', width=bar_width, edgecolor='grey', label='VR Gaming')

# Adding title and labels
ax.set_title('Sorted Futuristic Sports Ticket Sales in NeoCity (Year 2125)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Tickets Sold (Thousands)', fontsize=12)
ax.set_xticks([r + 1.5 * bar_width for r in range(len(seasons))])
ax.set_xticklabels(sorted_labels[0])

# Annotate each bar with ticket numbers
all_sales_sorted = sorted_labels[1:].flatten().astype(int)
for bar, ticket_sales in zip(ax.patches, all_sales_sorted):
    height = bar.get_height()
    ax.annotate(f'{ticket_sales}k', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, color='black')

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=11, title='Sports Events')

# Adjust layout and display the chart
plt.tight_layout()
plt.show()