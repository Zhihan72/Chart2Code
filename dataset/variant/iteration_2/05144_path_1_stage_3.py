import matplotlib.pyplot as plt

# Data for the box plot
solar_energy = [50, 55, 60, 65, 70, 72, 74, 76, 78, 80, 85]
wind_energy = [45, 50, 55, 60, 62, 64, 66, 68, 70, 75, 76]
hydroelectric_energy = [40, 42, 45, 47, 50, 53, 55, 57, 60, 64, 68]

data = [solar_energy, wind_energy, hydroelectric_energy]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create the vertical box plot
ax.boxplot(data, vert=True, patch_artist=True, notch=True,
           boxprops=dict(color='blue'),
           whiskerprops=dict(color='blue'),
           capprops=dict(color='blue'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

# Adding title and labels
plt.title("Renewable Energy Production Efficiency", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Energy Source", fontsize=12)
plt.ylabel("Yearly Production (in Gigawatts)", fontsize=12)

# Display the plot
plt.show()