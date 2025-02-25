import matplotlib.pyplot as plt
import numpy as np

# Constructing the data
engineering_hours = [15, 18, 21, 19, 20, 22, 24, 17, 16, 20, 23, 21, 19, 18, 17]
arts_hours = [10, 8, 12, 9, 11, 14, 15, 7, 10, 12, 13, 9, 11, 8, 10]
science_hours = [20, 22, 19, 24, 21, 23, 25, 18, 22, 21, 20, 22, 24, 19, 23]
business_hours = [5, 8, 7, 6, 9, 10, 8, 7, 6, 8, 9, 7, 10, 6, 8]
law_hours = [25, 28, 26, 29, 27, 30, 32, 26, 28, 29, 30, 27, 28, 25, 29]

# Data aggregation
data = [engineering_hours, arts_hours, science_hours, business_hours, law_hours]
majors = ["Engineering", "Arts", "Science", "Business", "Law"]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the box plot
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5,
                 boxprops=dict(facecolor="lightgreen", color="darkgreen"),
                 whiskerprops=dict(color="darkgreen"),
                 capprops=dict(color="darkgreen"),
                 flierprops=dict(marker="o", color="red", alpha=0.5),
                 medianprops=dict(color="darkorange"))

# Set colors for each box
colors = ['lightblue', 'lightpink', 'lightgray', 'lightyellow', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Remove titles and labels
ax.set_yticklabels([])  # Removes y-axis major group labels
ax.set_xticklabels([])  # Removes x-axis tick labels

# Add a horizontal grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Histogram subplot to show distribution
ax_hist = ax.twiny()
ax_hist.set_xticks([])
for i, data_series in enumerate(data):
    hist_data = np.histogram(data_series, bins=np.arange(min(data_series) - 1, max(data_series) + 2))
    ax_hist.barh([i + 1] * len(hist_data[0]), hist_data[0], left=hist_data[1][:-1], color=colors[i],
                 alpha=0.2, height=0.5)

# Adjust layout automatically
plt.tight_layout()

# Display the plot
plt.show()