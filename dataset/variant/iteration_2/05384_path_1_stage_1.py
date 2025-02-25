import numpy as np
import matplotlib.pyplot as plt

# Define attributes for the radar chart
attributes = ['Customer Service', 'Technical Support', 'Pricing', 'Coverage Area', 'Speed']

# Data for each brand of ISP
isp_1 = [6, 8, 5, 7, 9]
isp_2 = [8, 7, 7, 8, 8]
isp_3 = [5, 6, 9, 9, 7]
isp_4 = [9, 8, 8, 5, 6]

# Organize data
data = np.array([isp_1, isp_2, isp_3, isp_4])

# Number of variables
num_vars = len(attributes)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for plotting
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Single color for all ISPs
color = '#66b3ff'

# Plot each ISP
for i, isp_data in enumerate(data):
    ax.fill(angles, isp_data, color=color, alpha=0.25)
    ax.plot(angles, isp_data, label=f'ISP {i+1}', color=color, linewidth=2)

# Add attribute labels
plt.xticks(angles[:-1], attributes, color='grey', size=10)

# Add y-labels
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Title with multiple lines for better visibility
plt.title("Internet Service Providers Comparison:\nEvaluation of Various Attributes", size=16, weight='bold', position=(0.5, 1.1), ha='center')

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()