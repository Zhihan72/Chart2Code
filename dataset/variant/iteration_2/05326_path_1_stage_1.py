import matplotlib.pyplot as plt
import numpy as np

# Time period (days) of a month
days = np.arange(1, 31)

# Energy output data in kWh for three solar panels
panel_A = [50, 52, 48, 47, 49, 51, 53, 55, 54, 52, 53, 57, 59, 61, 60, 58, 57, 55, 56, 58, 60, 62, 64, 66, 65, 63, 62, 64, 65, 67]
panel_B = [45, 46, 44, 43, 45, 46, 47, 49, 50, 48, 49, 50, 51, 53, 54, 52, 51, 50, 52, 53, 55, 56, 58, 57, 56, 55, 54, 56, 57, 59]
panel_C = [40, 41, 39, 37, 38, 39, 42, 44, 45, 43, 41, 42, 43, 45, 44, 43, 41, 42, 44, 46, 47, 49, 50, 52, 51, 49, 48, 49, 50, 51]

# Create subplots figure
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the data for each remaining panel
ax1.plot(days, panel_A, label='Panel A', color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(days, panel_B, label='Panel B', color='green', marker='s', linestyle='--', linewidth=2)
ax1.plot(days, panel_C, label='Panel C', color='red', marker='^', linestyle='-.', linewidth=2)

# Adding title and labels
plt.title('Energy Output of SpaceX Solar Panels on the ISS\n Over a Month', fontsize=16, fontweight='bold')
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Energy Output (kWh)', fontsize=14)

# Adding grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax1.legend(title="Solar Panels", fontsize=12)

# Add annotations for specific data points for Panel A as a sample
important_days = [10, 15, 20, 25]
annotations = [
    "Solar flare interference",
    "Panel A maintenance",
    "Cosmic radiation spike",
    "Orientation adjustment"
]

for day, annotation in zip(important_days, annotations):
    ax1.annotate(annotation, xy=(day, panel_A[day-1]), xytext=(day, panel_A[day-1] + 5),
                 arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3,rad=.2"),
                 fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()