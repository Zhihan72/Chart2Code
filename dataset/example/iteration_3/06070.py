import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart illustrates the increase in average speeds of the fastest trains across various countries over several decades, showcasing advancements in high-speed rail technology.

# Decades for the x-axis
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Hypothetical data: Average speeds of fastest trains (in km/h) in different countries
japan_speeds = [130, 200, 240, 270, 300, 320, 350]
france_speeds = [120, 160, 200, 270, 300, 320, 330]
germany_speeds = [100, 150, 200, 250, 280, 300, 320]
china_speeds = [0, 0, 0, 200, 250, 300, 350]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the average speeds for each country
ax.plot(decades, japan_speeds, marker='o', label='Japan', linestyle='-', linewidth=2, color='red')
ax.plot(decades, france_speeds, marker='s', label='France', linestyle='--', linewidth=2, color='blue')
ax.plot(decades, germany_speeds, marker='^', label='Germany', linestyle='-.', linewidth=2, color='green')
ax.plot(decades, china_speeds, marker='d', label='China', linestyle=':', linewidth=2, color='purple')

# Add title and labels with multiple lines in the title for better visibility
ax.set_title('Advancements in High-Speed Rail Technology\nAverage Speeds of Fastest Trains (1960-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Average Speed (km/h)', fontsize=12)

# Customize ticks
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 401, 50))

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend with title
ax.legend(title='Countries', loc='upper left', fontsize=10)

# Annotate key milestones
milestones = {
    'Japan\nFirst Shinkansen': (1960, 130), 
    'France\nTGV Inauguration': (1980, 200), 
    'China\nCRH Introduction': (2000, 200)
}
for label, (x, y) in milestones.items():
    ax.annotate(label, xy=(x, y), xytext=(x, y+20),
                textcoords='data', ha='center',
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10)

# Automatically adjust layout for better visibility of elements
plt.tight_layout()

# Display the plot
plt.show()