import matplotlib.pyplot as plt

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Since the direction is to remove one or more data groups and there is only one, we will leave the data list as an empty plot 
# Set titles and labels
ax.set_title('Caloric Intake of Children (6-12) for 2023', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Caloric Intake (kcal)', fontsize=12)
ax.set_xticks([1])
ax.set_xticklabels(['Children (6-12)'], fontsize=12)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()