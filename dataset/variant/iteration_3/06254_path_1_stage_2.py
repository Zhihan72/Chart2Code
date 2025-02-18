import matplotlib.pyplot as plt
import numpy as np

# Original cities
original_cities = np.arange(1, 11)
green_space_per_capita_orig = np.array([15, 30, 25, 40, 50, 32, 22, 60, 45, 35])
happiness_index_orig = np.array([6.0, 7.5, 7.0, 8.0, 9.0, 7.2, 6.5, 9.5, 8.2, 7.8])

# Additional cities
additional_cities = np.arange(11, 21)
green_space_per_capita_add = np.array([10, 28, 24, 38, 48, 30, 20, 58, 42, 33])
happiness_index_add = np.array([5.5, 7.0, 6.8, 7.8, 8.8, 7.0, 6.3, 9.3, 8.0, 7.5])

# Create scatter plot
plt.figure(figsize=(12, 7))
plt.scatter(green_space_per_capita_orig, happiness_index_orig, color='royalblue', edgecolors='black', s=150, alpha=0.7, label='Original Cities')
plt.scatter(green_space_per_capita_add, happiness_index_add, color='forestgreen', edgecolors='black', s=150, alpha=0.7, label='Additional Cities')

# Annotations for original cities
for i, city in enumerate(original_cities):
    plt.annotate(f'City {city}', 
                 (green_space_per_capita_orig[i], happiness_index_orig[i]),
                 textcoords="offset points",
                 xytext=(5,5),
                 ha='center', fontsize=10, color='darkblue')  # changed color

# Annotations for additional cities
for i, city in enumerate(additional_cities):
    plt.annotate(f'City {city}', 
                 (green_space_per_capita_add[i], happiness_index_add[i]),
                 textcoords="offset points",
                 xytext=(5,5),
                 ha='center', fontsize=10, color='black')  # changed color

# Titles and labels
plt.title("Correlation Between Urban Green Space and Happiness Index\n Analysis of Various Global Cities", fontsize=16, fontweight='bold')
plt.xlabel("Urban Green Space per Capita (sqm)", fontsize=13)
plt.ylabel("Average Happiness Index (scale 1-10)", fontsize=13)

# Grid configuration to improve readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add trend lines for both groups
m_orig, b_orig = np.polyfit(green_space_per_capita_orig, happiness_index_orig, 1)
plt.plot(green_space_per_capita_orig, m_orig * green_space_per_capita_orig + b_orig, color='firebrick', linestyle='--', linewidth=2, label='Trend Line - Original')

m_add, b_add = np.polyfit(green_space_per_capita_add, happiness_index_add, 1)
plt.plot(green_space_per_capita_add, m_add * green_space_per_capita_add + b_add, color='darkorange', linestyle='--', linewidth=2, label='Trend Line - Additional')

# Add legend
plt.legend(loc='lower right')

# Automatically adjust layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()