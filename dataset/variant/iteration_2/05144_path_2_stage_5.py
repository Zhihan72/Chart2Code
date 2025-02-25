import matplotlib.pyplot as plt

# Altering the order of solar_energy to simulate randomness within the same dimensional structure
solar_energy = [72, 60, 70, 74, 85, 78, 50, 55, 76, 65, 80]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(6, 8))

# Generate a box plot for the single data group
ax.boxplot(solar_energy, vert=True, patch_artist=True,
           boxprops=dict(facecolor='skyblue', color='blue'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

# Set title and axis labels
plt.title("Solar Energy Output\nAnnual Distribution", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Solar Energy", fontsize=12)
plt.ylabel("Output (Gigawatts)", fontsize=12)

plt.tight_layout()
plt.show()