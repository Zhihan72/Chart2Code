import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the impact of different diets on monthly weight loss over a 6 month period
# We will examine distributions and trends of weight loss for various diet plans

# Define diet plans and weight loss data in kilograms
diets = ['Keto', 'Paleo', 'Vegan', 'Mediterranean', 'Intermittent Fasting']

# Weight loss data for 6 months (values in kilograms lost per month)
keto_weight_loss = [3.2, 3.1, 2.8, 2.9, 3.4, 3.3, 3.2, 2.9, 3.1, 3.0, 2.8, 3.1, 3.3, 3.0, 2.9, 3.0]
paleo_weight_loss = [3.0, 2.8, 3.2, 3.1, 2.9, 2.8, 3.0, 2.9, 3.1, 2.7, 2.8, 3.0, 2.9, 3.1, 3.0, 2.8]
vegan_weight_loss = [2.5, 2.4, 2.7, 2.8, 2.6, 2.4, 2.5, 2.6, 2.5, 2.3, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8]
mediterranean_weight_loss = [2.8, 2.9, 3.0, 2.7, 2.8, 3.1, 3.0, 2.9, 2.8, 3.0, 2.9, 2.7, 3.1, 2.9, 3.0, 2.8]
intermittent_fasting_weight_loss = [3.5, 3.7, 3.6, 3.9, 3.8, 3.7, 3.6, 3.5, 3.7, 3.9, 3.8, 3.7, 3.5, 3.6, 3.7, 3.8]

# Group all weight loss data
weight_loss_data = [
    keto_weight_loss, paleo_weight_loss,
    vegan_weight_loss, mediterranean_weight_loss,
    intermittent_fasting_weight_loss
]

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 10))

# Create box plots
bp = ax.boxplot(weight_loss_data, vert=True, notch=True, patch_artist=True,
                labels=diets, 
                boxprops=dict(facecolor='lightblue', color='blue', alpha=0.7),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                medianprops=dict(color='darkred', linewidth=2),
                flierprops=dict(marker='o', color='red', markersize=6, alpha=0.5))

# Add mean values
means = [np.mean(data) for data in weight_loss_data]
ax.scatter(range(1, len(means) + 1), means, color='green', zorder=3, label='Mean Weight Loss')

# Set the title and labels
ax.set_title('Weight Loss Analysis Across Different Diet Plans\nDistribution Over 6 Months', fontsize=16, fontweight='bold')
ax.set_ylabel('Weight Loss (kg)', fontsize=14)
ax.set_xlabel('Diet Plans', fontsize=14)

# Enhance readability with grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Add legend for the mean values
ax.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()