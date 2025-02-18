import matplotlib.pyplot as plt
import numpy as np

# Data for exoplanets
atmosphere_quality = [0.85, 0.90, 0.75, 0.70, 0.65, 0.80]
potential_habitability = [250, 270, 200, 300, 150, 180]

# Sort data based on potential habitability
sorted_indices = np.argsort(potential_habitability)
sorted_habitability = np.array(potential_habitability)[sorted_indices]
sorted_atmosphere_quality = np.array(atmosphere_quality)[sorted_indices]

# Set up the bar plot with a single color
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart with uniform color
ax.barh(range(len(sorted_habitability)), sorted_habitability, color='skyblue', align='center')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()