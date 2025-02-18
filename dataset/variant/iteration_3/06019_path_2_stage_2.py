import matplotlib.pyplot as plt
import numpy as np

# Define the decades from 1980 to 2020
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Computing power in millions of instructions per second (MIPS)
single_core_mips = np.array([1, 10, 100, 1000, 8000])
multi_core_mips = np.array([0, 0, 100, 3000, 15000])
gpu_acceleration_mips = np.array([0, 0, 0, 5000, 20000])
cloud_computing_mips = np.array([0, 0, 0, 0, 30000])

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, single_core_mips, multi_core_mips, gpu_acceleration_mips, cloud_computing_mips,
             labels=['Solo-chip Processors', 'Multiple-core Processing Units', 
                     'Graphical Processing Boost', 'Remote Computing'],
             colors=['#6A5ACD', '#FF6347', '#4682B4', '#32CD32'],  # Changed colors
             alpha=0.9)  # Changed alpha

# Set plot title and labels
ax.set_title('Transformation of Computing Capabilities\n(1980-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Era', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper right', title='Innovations', fontsize=10)  # Changed legend location and font size

# Format the x-axis to display decades nicely
ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=11)  # Changed font size

# Add grid lines for better readability
ax.grid(True, linestyle='-.', alpha=0.6)  # Changed grid line style and alpha

# Adjust figure borders
fig.patch.set_linewidth(2)  # Increased border width
fig.patch.set_edgecolor('gray')  # Changed border color

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()