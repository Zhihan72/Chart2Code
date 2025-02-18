import matplotlib.pyplot as plt
import numpy as np

# Backstory: Following the migration patterns of various bird species over a decade.
# Data on bird migrations across different regions

# Defining the years for the study period (2010-2020)
years = np.arange(2010, 2021)

# Constructing migration data for different bird species across various regions
sparrows = np.array([200, 300, 400, 550, 700, 850, 950, 1100, 1250, 1400, 1500])
hawks = np.array([100, 200, 300, 350, 400, 450, 500, 550, 600, 700, 750])
swallows = np.array([300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1100])
pelicans = np.array([50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 250])
geese = np.array([100, 150, 200, 350, 500, 600, 700, 800, 900, 1000, 1100])

# Combine data for the area chart
bird_migrations = np.vstack([sparrows, hawks, swallows, pelicans, geese])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define custom colors for each bird species
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot the stacked area chart
ax.stackplot(years, bird_migrations, labels=['Sparrows', 'Hawks', 'Swallows', 'Pelicans', 'Geese'], 
             colors=colors, alpha=0.8)

# Setting the title and labels
ax.set_title("Decade of Bird Migrations Across Regions (2010-2020)\nTracking Various Bird Species", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Birds", fontsize=12)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding annotations for key events
ax.annotate('Increase in Sparrow Population', xy=(2013, 700), xytext=(2010, 1600),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Hawk Migration Peak', xy=(2019, 700), xytext=(2017, 1400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adding a legend outside the plot
ax.legend(loc='upper left', fontsize=10, title='Bird Species', bbox_to_anchor=(1.05, 1))

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Adjusting layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Showing the plot
plt.show()