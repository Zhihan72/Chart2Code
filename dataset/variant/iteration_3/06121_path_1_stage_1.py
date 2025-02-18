import matplotlib.pyplot as plt
import numpy as np

# Define the data
snack_types = ['Chips', 'Chocolate', 'Fruits', 'Cookies', 'Candy', 'Others']
preferences = [25, 20, 15, 15, 15, 10]

# Define colors for each segment of the pie chart with different shades
colors = ['#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', '#32CD32', '#00CED1']

# No highlighting of slices through explode
explode = (0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=snack_types, 
    autopct='%1.0f%%', 
    startangle=45,  # Changed the starting angle
    colors=colors, 
    explode=explode, 
    shadow=False,  # Removed shadow
    textprops=dict(color="black", fontsize=10, weight="semibold"),  # Altered text properties
    wedgeprops=dict(edgecolor='navy', linewidth=2, linestyle='--')  # Changed border style
)

# Set the title
plt.title('Favorite Snack Types Among Students\nSurvey 2023', fontsize=18, fontstyle='italic', pad=30)

# Add a legend in a different position
plt.legend(wedges, snack_types, title="Snacks", loc="upper right", fontsize=10)

# The pie chart is not forced to be a perfect circle
plt.axis('auto')

# Automatically adjust layout to ensure sufficient padding is maintained
plt.tight_layout()

# Display the plot
plt.show()