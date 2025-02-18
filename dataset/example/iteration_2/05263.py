import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In 2023, the Global Innovation Summit showcased the technological strides in different areas among various regions.
# One particular interest was the rapid growth in the adoption of various technologies in North America, Europe, and Asia.

# Defining the regions
regions = ['North America', 'Europe', 'Asia']

# Fictional adoption data for various technologies (in %)
AI_adoption_rate = [45, 50, 60]         # Percentage of businesses using AI
IoT_adoption_rate = [55, 65, 70]        # Percentage of businesses using IoT
Blockchain_adoption_rate = [25, 35, 45] # Percentage of businesses using Blockchain
Quantum_adoption_rate = [10, 20, 30]    # Percentage of businesses using Quantum Computing

# Data Grouping
adoption_data = np.array([AI_adoption_rate, IoT_adoption_rate, Blockchain_adoption_rate, Quantum_adoption_rate])
technologies = ['AI', 'IoT', 'Blockchain', 'Quantum Computing']

# Set up the plot with two subplots: one for the bar plot, another for a pie chart breakdown
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Bar Plot for the adoption rates across regions
x = np.arange(len(regions))  # Label locations
width = 0.2                  # Bar width
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']  # Colors for different technologies

# Plotting bars for each technology
for i in range(len(adoption_data)):
    ax1.bar(x + i * width, adoption_data[i], width, label=technologies[i], color=colors[i])

# Title and labels
ax1.set_title('Tech Adoption Rates by Region (2023)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Adoption Rate (%)', fontsize=12)
ax1.set_xticks(x + width * 1.5)
ax1.set_xticklabels(regions)
ax1.legend(title='Technology', fontsize=11, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations
for i in range(len(adoption_data)):
    for j in range(len(regions)):
        ax1.annotate(f'{adoption_data[i, j]}%',
                     xy=(x[j] + i * width, adoption_data[i, j]),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10)

# Pie Chart showing the overall percentage of each technology across all regions
total_adoption = np.sum(adoption_data, axis=1)
ax2.pie(total_adoption, labels=technologies, colors=colors, autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})

# Title for the pie chart
ax2.set_title('Overall Tech Adoption Breakdown (2023)', fontsize=14, fontweight='bold')

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()