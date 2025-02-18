import matplotlib.pyplot as plt

# Data for fuel consumption (liters per 100km) for different vehicle types from 2000 to 2020
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]
suvs = [12.0, 11.8, 11.5, 11.3, 11.0, 10.7, 10.5, 10.3, 10.0, 9.8, 9.5, 9.3, 9.0, 8.8, 8.5, 8.3, 8.0, 7.8, 7.5, 7.3, 7.0]
trucks = [14.0, 13.8, 13.6, 13.4, 13.2, 13.0, 12.8, 12.6, 12.4, 12.2, 12.0, 11.8, 11.6, 11.4, 11.2, 11.0, 10.8, 10.6, 10.4, 10.2, 10.0]

# List of data groups
data = [sedans, suvs, trucks]

# Create the vertical boxplot for multiple groups
plt.figure(figsize=(8, 8))
plt.boxplot(data, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='navy'),
            whiskerprops=dict(color='navy'),
            capprops=dict(color='navy'),
            medianprops=dict(color='darkorange', linewidth=2),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Title and labels
plt.title("Fuel Efficiency for Different Vehicle Types (2000-2020)", fontsize=14, fontweight='bold')
plt.ylabel("Fuel Consumption (Liters per 100km)", fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['Sedans', 'SUVs', 'Trucks'])

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()