import matplotlib.pyplot as plt
import numpy as np

wonders = [
    "Pyramid of Giza", "Lighthouse", 
    "Gardens of Babylon", "Artemis Temple", "Colossus"
]

tourists = np.array([450, 410, 380, 310, 290])

colors = ['#8A2BE2', '#87CEEB', '#5F9EA0', '#FF69B4', '#ADFF2F']

# Create a bar chart with sorted data
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(wonders, tourists, color=colors, edgecolor='darkgrey', hatch='/')

# Annotate the bars with their respective values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='navy')

# Configure chart title and labels
ax.set_title('Tourists in 100 AD: Ancient Wonders (Sorted)', fontsize=18, pad=30)
ax.set_xlabel('Ancient Wonders', fontsize=14, style='italic')
ax.set_ylabel('Tourists (thousands)', fontsize=14, style='italic')

# Rotate x-ticks for better readability
plt.xticks(rotation=30, ha='right')

# Add a grid for better clarity
ax.yaxis.grid(True, linestyle='-.', linewidth=0.5)

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()