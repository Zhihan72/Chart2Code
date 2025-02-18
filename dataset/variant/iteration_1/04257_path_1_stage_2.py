import matplotlib.pyplot as plt
import squarify

# Energy sources and contributions
energy_sources = [
    'Solar Power', 
    'Wind Power', 
    'Hydro Power', 
    'Geothermal Energy', 
    'Biomass Energy'
]

contributions = [450, 200, 300, 100, 150]

# Normalize contributions for the treemap
total_contribution = sum(contributions)
sizes = [c / total_contribution * 100 for c in contributions]

# Set colors for each energy source
colors = ['#FFD700', '#87CEFA', '#7FFFD4', '#FF4500', '#8B4513']

# Create the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Create the treemap with altered stylistic elements
squarify.plot(sizes=sizes, label=[f"{source}\n{size:.1f}%" for source, size in zip(energy_sources, sizes)],
              color=colors, alpha=0.7, edgecolor="black", linewidth=1.5, 
              text_kwargs={'fontsize': 11, 'weight': 'normal', 'color': 'black'})

# Random change in stylistic elements
plt.title("Futuristic City Power Grid: Renewable Energy Distribution", fontsize=18, fontstyle='italic')
plt.axhline(y=0.5, color='gray', linestyle='--')  # Add a horizontal line
plt.axvline(x=0.5, color='gray', linestyle='--')  # Add a vertical line
plt.axis('off')

plt.tight_layout()

# Display the plot
plt.show()