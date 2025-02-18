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
             colors=['#FFD700', '#87CEFA', '#2E8B57', '#D2691E'],
             alpha=0.8)

# Set plot title and labels
ax.set_title('Transformation of Computing Capabilities\n(1980-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Era', fontsize=12)
ax.set_ylabel('MIPS (Million of Instructions per Second)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', title='Innovations')

# Format the x-axis to display decades nicely
ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()