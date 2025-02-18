import matplotlib.pyplot as plt
import numpy as np

# Data for Vitamin A (in micrograms)
vitamin_a_apples = np.array([54, 60, 63, 65, 59, 70, 65, 62, 55, 66])
vitamin_a_bananas = np.array([30, 28, 32, 31, 29, 33, 27, 26, 34, 30])
vitamin_a_oranges = np.array([98, 102, 110, 95, 105, 107, 103, 109, 101, 98])

# Data for Vitamin C (in milligrams)
vitamin_c_apples = np.array([6, 7, 8, 9, 5, 10, 7, 6, 8, 9])
vitamin_c_bananas = np.array([9, 8, 10, 11, 7, 12, 10, 9, 8, 12])
vitamin_c_oranges = np.array([50, 45, 55, 48, 60, 62, 51, 58, 59, 57])

# Data for Vitamin E (in milligrams)
vitamin_e_apples = np.array([0.5, 0.6, 0.45, 0.5, 0.6, 0.65, 0.55, 0.52, 0.48, 0.50])
vitamin_e_bananas = np.array([0.2, 0.15, 0.18, 0.22, 0.20, 0.19, 0.21, 0.23, 0.24, 0.18])
vitamin_e_oranges = np.array([0.8, 0.75, 0.85, 0.77, 0.80, 0.87, 0.76, 0.82, 0.81, 0.79])

# Aggregate data for box plot
vitamin_data_a = [vitamin_a_apples, vitamin_a_bananas, vitamin_a_oranges]
vitamin_data_c = [vitamin_c_apples, vitamin_c_bananas, vitamin_c_oranges]
vitamin_data_e = [vitamin_e_apples, vitamin_e_bananas, vitamin_e_oranges]

# Labels for fruits
fruit_labels = ['Apples', 'Bananas', 'Oranges']

# Plot setup
fig, axs = plt.subplots(1, 3, figsize=(18, 8))

# First subplot: Vitamin A Distribution
axs[0].boxplot(vitamin_data_a, vert=False, patch_artist=True, labels=fruit_labels, notch=True,
               boxprops=dict(facecolor='deepskyblue', color='dodgerblue'),
               whiskerprops=dict(color='dodgerblue'),
               capprops=dict(color='dodgerblue'),
               medianprops=dict(color='darkorange', linewidth=1.5))
axs[0].set_title('Vitamin A Distribution in Fruits', fontsize=16, weight='bold', pad=20)
axs[0].set_xlabel('Vitamin A (micrograms)', fontsize=12)
axs[0].set_ylabel('Fruit Types', fontsize=12)
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Second subplot: Vitamin C Distribution
axs[1].boxplot(vitamin_data_c, vert=False, patch_artist=True, labels=fruit_labels, notch=True,
               boxprops=dict(facecolor='mediumpurple', color='indigo'),
               whiskerprops=dict(color='indigo'),
               capprops=dict(color='indigo'),
               medianprops=dict(color='gold', linewidth=1.5))
axs[1].set_title('Vitamin C Distribution in Fruits', fontsize=16, weight='bold', pad=20)
axs[1].set_xlabel('Vitamin C (milligrams)', fontsize=12)
axs[1].set_ylabel('Fruit Types', fontsize=12)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Third subplot: Vitamin E Distribution
axs[2].boxplot(vitamin_data_e, vert=False, patch_artist=True, labels=fruit_labels, notch=True,
               boxprops=dict(facecolor='darkgoldenrod', color='goldenrod'),
               whiskerprops=dict(color='goldenrod'),
               capprops=dict(color='goldenrod'),
               medianprops=dict(color='darkslategray', linewidth=1.5))
axs[2].set_title('Vitamin E Distribution in Fruits', fontsize=16, weight='bold', pad=20)
axs[2].set_xlabel('Vitamin E (milligrams)', fontsize=12)
axs[2].set_ylabel('Fruit Types', fontsize=12)
axs[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Adjust layout for a better fit
plt.tight_layout()

# Show plot
plt.show()