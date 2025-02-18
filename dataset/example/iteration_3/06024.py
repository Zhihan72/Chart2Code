import matplotlib.pyplot as plt
import numpy as np

# Backstory: We're analyzing the transportation preferences of a small town's residents. 
# The data shows the percentage that each mode of transportation is used during weekdays and weekends.
modes_of_transport = ['Bicycles', 'Cars', 'Public Transport', 'Walking', 'Motorcycles']
weekday_usage = [20, 40, 25, 10, 5]
weekend_usage = [25, 30, 20, 20, 5]

# Colors for the different modes of transportation
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice to highlight Bicycles on the first chart

# Create subplots: one for weekday usage and one for weekend usage
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the weekday pie chart
wedges1, texts1, autotexts1 = ax1.pie(
    weekday_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize label and text appearance for the weekday chart
plt.setp(texts1, size=10, weight='bold')
plt.setp(autotexts1, size=9, weight='bold', color='white')

# Title for the weekday pie chart
ax1.set_title("Weekday Transportation Preferences", fontsize=14, fontweight='bold', pad=20)
ax1.axis('equal')

# Add legend for the weekday chart
ax1.legend(wedges1, modes_of_transport, title="Mode of Transport", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# Plot the weekend pie chart
wedges2, texts2, autotexts2 = ax2.pie(
    weekend_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize label and text appearance for the weekend chart
plt.setp(texts2, size=10, weight='bold')
plt.setp(autotexts2, size=9, weight='bold', color='white')

# Title for the weekend pie chart
ax2.set_title("Weekend Transportation Preferences", fontsize=14, fontweight='bold', pad=20)
ax2.axis('equal')

# Add legend for the weekend chart
ax2.legend(wedges2, modes_of_transport, title="Mode of Transport", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# Main title for the overall chart
fig.suptitle("Town Residents' Transportation Habits", fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()