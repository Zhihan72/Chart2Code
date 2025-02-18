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

# Plotting a horizontal boxplot
box = ax.boxplot(data, vert=False, patch_artist=True, notch=False, whis=1.2,
                 boxprops=dict(facecolor='lightblue', color="navy"),
                 whiskerprops=dict(color="darkred"),
                 capprops=dict(color="purple"),
                 flierprops=dict(marker="*", color="orange", alpha=0.6),
                 medianprops=dict(color="black"))

# Add titles and labels
ax.set_title("Weekly Reading Hours\nby Major", fontsize=18, fontweight='medium')
ax.set_xlabel("Hours/Week", fontsize=12)
ax.set_yticklabels(majors, fontsize=12)

# Change grid style and add border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

# Adjust layout automatically
plt.tight_layout()

# Display the plot
plt.show()