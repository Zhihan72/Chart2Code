import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

# Define average screen sizes in inches
avg_screen_sizes = np.array([3.5, 3.7, 4.0, 4.5, 4.7, 5.0, 5.2, 5.5, 5.7, 6.1, 6.4])

# Define screen sizes for notable models
notable_models = {"iPhone 4": (2010, 3.5), "Samsung S3": (2012, 4.8), 
                  "iPhone 6": (2014, 4.7), "Samsung S8": (2017, 5.8), "iPhone 11": (2019, 6.1)}

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the average screen sizes over the years
ax.plot(years, avg_screen_sizes, color='orange', marker='o', linestyle='-', linewidth=2, label='Avg Screen Size')

# Highlight notable smartphone models
for model, (year, size) in notable_models.items():
    ax.plot(year, size, color='purple', marker='o')  # Purple dot for notable models
    ax.text(year, size + 0.1, model, color='purple', ha='center', fontsize=10)

# Titles and labels
plt.title('Evolution of Smartphone Screen Sizes (2010 - 2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Screen Size (inches)', fontsize=12)

# Customize x-ticks and y-ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(3.0, 7.0, 0.5))

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()