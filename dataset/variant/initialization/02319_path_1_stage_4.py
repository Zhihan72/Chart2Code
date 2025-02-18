import matplotlib.pyplot as plt
import numpy as np

initial_emissions = 10000
emissions_changes = np.array([
    -1500, 
    -1200, 
    -800,   
    -500,   
    300     
])

new_emissions_changes = np.array([
    -200,   
    -700,    
    100     
])

# Combine original and new data arrays
combined_emissions_changes = np.concatenate((emissions_changes, new_emissions_changes), axis=0)

emissions_positions = np.zeros(len(combined_emissions_changes) + 1)
emissions_positions[0] = initial_emissions
for i in range(1, len(emissions_positions)):
    emissions_positions[i] = emissions_positions[i-1] + combined_emissions_changes[i-1]

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(range(len(emissions_positions)), emissions_positions, color='#808080')

# Remove legends, grids, and borders
ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.tight_layout()
plt.show()