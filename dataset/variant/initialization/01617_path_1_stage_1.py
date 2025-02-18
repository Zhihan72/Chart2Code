import matplotlib.pyplot as plt
import numpy as np

# Years for the dataset
years = np.arange(2010, 2021)

# Enrollment data for each discipline in social sciences and humanities
enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
    "Philosophy": [240, 250, 260, 280, 300, 320, 330, 340, 350, 360, 370],
    "Literature": [220, 230, 240, 250, 270, 290, 310, 320, 330, 340, 350],
}

# Colors for different disciplines
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Initialize the plot
fig, ax = plt.subplots(figsize=(16, 10))

# Set x positions for bars
x = np.arange(len(years))

# Calculate negative and positive side stackings
neg_offsets = np.zeros_like(years)
pos_offsets = np.zeros_like(years)

# Plotting diverging bars
for i, (discipline, counts) in enumerate(enrollments.items()):
    pos_bars = np.array(counts) > 340
    ax.barh(x[pos_bars], np.array(counts)[pos_bars] - 340, left=pos_offsets[pos_bars], color=colors[i], label=discipline)
    pos_offsets[pos_bars] += np.array(counts)[pos_bars] - 340

    ax.barh(x[~pos_bars], 340 - np.array(counts)[~pos_bars], left=neg_offsets[~pos_bars], color=colors[i])
    neg_offsets[~pos_bars] += 340 - np.array(counts)[~pos_bars]

# Central axis indicator
ax.axvline(0, color='grey', linestyle='--', linewidth=0.8)

# Set title and labels
ax.set_title("Diverging Bar Chart of Student Enrollments from 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Number of Enrollments (Deviation from 340)", fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(years, fontsize=10)

# Add legend outside the plot for better readability
ax.legend(title="Disciplines", loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()