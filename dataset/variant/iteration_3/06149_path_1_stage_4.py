import matplotlib.pyplot as plt

# Create an empty figure and axis as the data is removed
fig, ax = plt.subplots(figsize=(6, 8))

# Set labels for consistency, even though no data will be displayed
ax.set_ylabel('Sleep Hours per Night', fontsize=12)
ax.set_xticklabels(['Basketball'], fontsize=11, fontweight='bold')

# Adjust layout and show plot
plt.tight_layout()
plt.show()