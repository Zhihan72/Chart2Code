import matplotlib.pyplot as plt
import numpy as np

# Data
seasons = ['Winter', 'Autumn', 'Spring', 'Summer']
apples_consumption = [220, 150, 180, 130]

# Sort the data
sorted_indices = np.argsort(apples_consumption)
sorted_seasons = [seasons[i] for i in sorted_indices]
sorted_apples_consumption = [apples_consumption[i] for i in sorted_indices]

# Create the sorted bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(sorted_seasons, sorted_apples_consumption, color='#FF6347')

# Add text labels above the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9)

# Set labels and title
ax.set_xlabel('Fruit Seasons', fontsize=12)
ax.set_ylabel('Apples Eaten (kg)', fontsize=12)
ax.set_title('Apples Eaten by Each Season', fontsize=16, fontweight='bold', pad=15)

# Add gridlines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()