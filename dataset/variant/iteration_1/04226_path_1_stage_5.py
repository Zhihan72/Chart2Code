import matplotlib.pyplot as plt
import numpy as np

# Data for Vitamin A (in micrograms)
vitamin_a_apples = np.array([54, 60, 63, 65, 59, 70, 65, 62, 55, 66])
vitamin_a_bananas = np.array([30, 28, 32, 31, 29, 33, 27, 26, 34, 30])
vitamin_a_oranges = np.array([98, 102, 110, 95, 105, 107, 103, 109, 101, 98])
vitamin_a_grapes = np.array([25, 26, 30, 29, 28, 27, 31, 32, 34, 30])

# Data for Vitamin C (in milligrams)
vitamin_c_apples = np.array([6, 7, 8, 9, 5, 10, 7, 6, 8, 9])
vitamin_c_bananas = np.array([9, 8, 10, 11, 7, 12, 10, 9, 8, 12])
vitamin_c_oranges = np.array([50, 45, 55, 48, 60, 62, 51, 58, 59, 57])
vitamin_c_grapes = np.array([4, 5, 6, 5, 7, 6, 4, 8, 5, 7])

# Aggregate data for box plot
vitamin_data_a = [vitamin_a_apples, vitamin_a_bananas, vitamin_a_oranges, vitamin_a_grapes]
vitamin_data_c = [vitamin_c_apples, vitamin_c_bananas, vitamin_c_oranges, vitamin_c_grapes]

# Labels for fruits
fruit_labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']

# Plot setup
fig, axs = plt.subplots(1, 2, figsize=(12, 8))

# First subplot: Vitamin A Distribution
axs[0].boxplot(vitamin_data_a, vert=False, patch_artist=True, labels=fruit_labels, notch=True)
axs[0].set_title('Vitamin A Distribution in Fruits', fontsize=16, weight='bold', pad=20)
axs[0].set_xlabel('Vitamin A (micrograms)', fontsize=12)
axs[0].set_ylabel('Fruit Types', fontsize=12)

# Second subplot: Vitamin C Distribution
axs[1].boxplot(vitamin_data_c, vert=False, patch_artist=True, labels=fruit_labels, notch=True)
axs[1].set_title('Vitamin C Distribution in Fruits', fontsize=16, weight='bold', pad=20)
axs[1].set_xlabel('Vitamin C (milligrams)', fontsize=12)
axs[1].set_ylabel('Fruit Types', fontsize=12)

# Adjust layout for a better fit
plt.tight_layout()

# Show plot
plt.show()