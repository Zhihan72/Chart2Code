import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]

# Original labels for clarity, could be shuffled
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']

# Create a bar chart (vertical)
fig, ax = plt.subplots(figsize=(14, 8))
x_pos = np.arange(len(social_media))  # The bar locations

# Plotting bars for social_media and gaming
ax.bar(x_pos, social_media, width=0.4, label='Social Media', color='slateblue')
ax.bar(x_pos + 0.4, gaming, width=0.4, label='Gaming', color='skyblue')

# Set the category labels
ax.set_xticks(x_pos + 0.2)
ax.set_xticklabels(categories)

# Adding a legend
ax.legend()

# Displaying the plot
plt.tight_layout()
plt.show()