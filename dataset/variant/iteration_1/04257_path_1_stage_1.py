import matplotlib.pyplot as plt
import squarify

# Define the renewable energy sources and their contributions to the city's power grid in MW
energy_sources = [
    'Solar Power', 
    'Wind Power', 
    'Hydro Power', 
    'Geothermal Energy', 
    'Biomass Energy'
]

# Swapped contributions to randomly alter the content
contributions = [450, 200, 300, 100, 150]

# Normalize the contributions for use in the treemap
total_contribution = sum(contributions)
sizes = [c / total_contribution * 100 for c in contributions]

# Define colors for each energy source
colors = ['#FFD700', '#87CEFA', '#7FFFD4', '#FF4500', '#8B4513']

# Create the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Create the treemap
squarify.plot(sizes=sizes, label=[f"{source}\n{size:.1f}%" for source, size in zip(energy_sources, sizes)],
              color=colors, alpha=0.8, edgecolor="white", linewidth=2, 
              text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'})

# Customize the title and layout
plt.title("Futuristic City Power Grid: Renewable Energy Distribution", fontsize=16, fontweight='bold')
plt.axis('off')  # Hide axes

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()