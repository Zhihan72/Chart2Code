import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are comparing the production efficiency of different renewable energy sources over a decade.

# Define the data for the box plot
# Each list represents yearly productivity (in gigawatts) over a decade for various renewable energy sources
solar_energy = [50, 55, 60, 65, 70, 72, 74, 76, 78, 80, 85]
wind_energy = [45, 50, 55, 60, 62, 64, 66, 68, 70, 75, 76]
hydroelectric_energy = [40, 42, 45, 47, 50, 53, 55, 57, 60, 64, 68]
geothermal_energy = [30, 32, 34, 36, 37, 40, 42, 44, 45, 48, 50]

# Combine data into a list for plotting
data = [solar_energy, wind_energy, hydroelectric_energy, geothermal_energy]
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric Energy', 'Geothermal Energy']

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create the vertical box plot
boxplot = ax.boxplot(data, vert=True, patch_artist=True, notch=True,
                    boxprops=dict(facecolor='skyblue', color='blue'),
                    whiskerprops=dict(color='blue'),
                    capprops=dict(color='blue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

# Customizing colors for each energy source
colors = ['#FFD700', '#90EE90', '#1E90FF', '#FF6347']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Adding title and labels
plt.title("Renewable Energy Production Efficiency\nComparative Analysis of Different Sources (2010-2020)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Energy Source", fontsize=12)
plt.ylabel("Yearly Production (in Gigawatts)", fontsize=12)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Customizing other plot elements to enhance clarity
plt.setp(boxplot['whiskers'], color='black', linestyle='-', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='red', linewidth=2)

# Highlighting the overall mean production across all energy sources with a horizontal line
overall_mean = np.mean(solar_energy + wind_energy + hydroelectric_energy + geothermal_energy)
ax.axhline(overall_mean, color='green', linestyle='--', linewidth=1.5, label='Overall Average Production')

# Adding a legend
ax.legend(loc='upper left', fontsize=10)

# Ensure the layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()