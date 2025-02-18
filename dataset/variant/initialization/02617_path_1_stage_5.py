import matplotlib.pyplot as plt

# Define the yield data
wheat_yield = [3.1, 2.8, 3.0, 3.3, 2.4, 3.5, 2.5, 3.2, 2.7, 2.9]
corn_yield = [5.2, 5.0, 6.0, 5.8, 5.1, 5.4, 6.2, 5.3, 5.5, 5.7]
rice_yield = [4.6, 4.5, 4.3, 4.1, 4.0, 4.2, 4.8, 4.4, 4.5, 4.0]
soy_yield = [3.6, 3.5, 3.3, 3.7, 3.2, 3.1, 3.0, 3.9, 3.4, 3.8]
cotton_yield = [2.1, 2.3, 1.8, 2.0, 2.2, 1.9, 2.5, 2.0, 2.4, 2.1]

# Prepare data for a single group box plot
data = [wheat_yield, corn_yield, rice_yield, soy_yield, cotton_yield]

fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the vertical box plot for a single group of data
ax.boxplot(data, vert=True, patch_artist=True)

# Set labels
ax.set_xticklabels(['Wheat', 'Corn', 'Rice', 'Soy', 'Cotton'])
ax.set_ylabel('Yield (t/ha)')
ax.set_xlabel('Crop')

plt.tight_layout()
plt.show()