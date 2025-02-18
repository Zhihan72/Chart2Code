import matplotlib.pyplot as plt

# Data for fuel consumption (liters per 100km) for different vehicle types from 2000 to 2020
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]

# Create the vertical boxplot for a single group
plt.figure(figsize=(6, 8))
plt.boxplot(sedans, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='navy'),
            whiskerprops=dict(color='navy'),
            capprops=dict(color='navy'),
            medianprops=dict(color='darkorange', linewidth=2),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Title and labels
plt.title("Fuel Efficiency for Sedans (2000-2020)", fontsize=14, fontweight='bold')
plt.ylabel("Fuel Consumption (Liters per 100km)", fontsize=12)
plt.xticks(ticks=[1], labels=['Sedans'])

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()