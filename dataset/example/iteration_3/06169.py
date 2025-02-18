import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking environmental impact of e-waste recycling programs in different regions. 
# This chart will compare amounts of materials recovered through e-waste recycling.

# Regions
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# E-waste material recovery data (in metric tons)
# Format: [Metals, Plastics, Glass, Electronics]
na_recovery = [4500, 3500, 2500, 500]
eu_recovery = [5000, 4500, 3000, 600]
asia_recovery = [9000, 8000, 6000, 1200]
sa_recovery = [2000, 1500, 1000, 300]
africa_recovery = [1000, 800, 700, 150]

# Compile all data into a list for ease of plotting
data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

# Plotting a stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Bar colors for each material type
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the bar positions and width
bar_positions = np.arange(len(regions))
bar_width = 0.6

# Initialize the bottom positions for stacks
bottoms = np.zeros(len(regions))

# Plot the stacked bars
for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, label=['Metals', 'Plastics', 'Glass', 'Electronics'][i],
           color=colors[i], bottom=bottoms, alpha=0.8)
    bottoms += data[:, i]

# Add titles and labels
ax.set_title('Regional E-Waste Recycling Impact in 2023:\nMaterial Recovery Breakdown', fontsize=16, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Recovered Materials (Metric Tons)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(regions, fontsize=10)
ax.set_ylim(0, max(data.sum(axis=1)) * 1.1)

# Add legend
ax.legend(title='Recovered Material Type', fontsize=10)

# Add values above bars
for i, region_data in enumerate(data):
    cumulative = 0
    for j, amount in enumerate(region_data):
        ax.text(i, cumulative + amount / 2, f'{amount}', ha='center', va='center', fontsize=9, color='white')
        cumulative += amount

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()