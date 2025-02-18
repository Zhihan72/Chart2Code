import numpy as np
import matplotlib.pyplot as plt

# Define sectors of renewable energy
sectors = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']

# Define regions with renewable energy proficiency
regions = ['North America', 'Europe', 'Asia', 'Oceania', 'Africa']

# Renewable energy adoption scores
# Scores are in percentage form, representing the proportion of total energy production
data = {
    'North America': [40, 25, 20, 10, 5],
    'Europe': [35, 30, 20, 10, 5],
    'Asia': [30, 25, 30, 10, 5],
    'Oceania': [25, 20, 15, 30, 10],
    'Africa': [20, 15, 10, 25, 30]
}

# Aggregate data into an array
data_array = np.array([data[region] for region in regions])

# Function to create a radar chart
def create_radar_chart(sectors, data, title, region_colors):
    num_vars = len(sectors)

    # Calculate angles for the radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the plot

    # Initialize the radar chart
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Draw one axe per variable and add labels
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sectors, fontsize=12, color='darkblue')

    # Plot data for each region
    for idx, (region, values) in enumerate(data.items()):
        values += values[:1]  # Close the plot
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=region_colors[idx])
        ax.fill(angles, values, color=region_colors[idx], alpha=0.25)

    # Add title and legend
    plt.title(title, size=16, weight='bold', color='navy', va='bottom', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10, title="Regions", title_fontsize=12)

    # Customize radial grid and labels
    ax.yaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.xaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(['10%', '20%', '30%', '40%', '50%'], color='gray', size=12)

    # Remove the polar spine for a cleaner look
    ax.spines['polar'].set_visible(False)

    # Automatically adjust layout for readability
    plt.tight_layout()
    plt.show()

# Define region-specific colors
region_colors = ['#FFD700', '#00FF00', '#00FFFF', '#FF00FF', '#FF4500']

# Create and display the radar chart
title = "Renewable Energy Adoption Trends Across Global Regions"
create_radar_chart(sectors, data, title, region_colors)