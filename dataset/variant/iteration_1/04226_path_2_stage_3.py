import matplotlib.pyplot as plt
import numpy as np

vitamin_a_apples = np.array([54, 60, 63, 65, 59, 70, 65, 62, 55, 66])
vitamin_a_oranges = np.array([98, 102, 110, 95, 105, 107, 103, 109, 101, 98])
vitamin_c_apples = np.array([6, 7, 8, 9, 5, 10, 7, 6, 8, 9])
vitamin_c_oranges = np.array([50, 45, 55, 48, 60, 62, 51, 58, 59, 57])
vitamin_e_apples = np.array([0.5, 0.6, 0.45, 0.5, 0.6, 0.65, 0.55, 0.52, 0.48, 0.50])
vitamin_e_oranges = np.array([0.8, 0.75, 0.85, 0.77, 0.80, 0.87, 0.76, 0.82, 0.81, 0.79])

vitamin_data_a = [vitamin_a_apples, vitamin_a_oranges]
vitamin_data_c = [vitamin_c_apples, vitamin_c_oranges]
vitamin_data_e = [vitamin_e_apples, vitamin_e_oranges]

fruit_labels = ['Apples', 'Oranges']

fig, axs = plt.subplots(3, 1, figsize=(8, 14))

axs[0].boxplot(vitamin_data_a, vert=False, patch_artist=True, labels=fruit_labels, notch=False,
               boxprops=dict(facecolor='skyblue', color='blue'),
               whiskerprops=dict(color='blue'),
               capprops=dict(color='blue'),
               medianprops=dict(color='green', linewidth=2.0))
for patch in axs[0].patches:
    patch.set_facecolor('lightgrey')
axs[0].set_title('Vitamin A in Fruits', fontsize=14, pad=15)
axs[0].set_xlabel('Vitamin A (micrograms)', fontsize=10)
axs[0].set_ylabel('Fruit Types', fontsize=10)
axs[0].grid(True, linestyle='-', linewidth=0.8, alpha=0.5, axis='x')

axs[1].boxplot(vitamin_data_c, vert=False, patch_artist=True, labels=fruit_labels, notch=False,
               boxprops=dict(facecolor='lightpink', color='red'),
               whiskerprops=dict(color='red'),
               capprops=dict(color='red'),
               medianprops=dict(color='purple', linewidth=2.0))
for patch in axs[1].patches:
    patch.set_facecolor('azure')
axs[1].set_title('Vitamin C in Fruits', fontsize=14, pad=15)
axs[1].set_xlabel('Vitamin C (milligrams)', fontsize=10)
axs[1].set_ylabel('Fruit Types', fontsize=10)
axs[1].grid(False)

axs[2].boxplot(vitamin_data_e, vert=False, patch_artist=True, labels=fruit_labels, notch=False,
               boxprops=dict(facecolor='lightyellow', color='orange'),
               whiskerprops=dict(color='orange'),
               capprops=dict(color='orange'),
               medianprops=dict(color='deepskyblue', linewidth=2.0))
for patch in axs[2].patches:
    patch.set_facecolor('mistyrose')
axs[2].set_title('Vitamin E in Fruits', fontsize=14, pad=15)
axs[2].set_xlabel('Vitamin E (milligrams)', fontsize=10)
axs[2].set_ylabel('Fruit Types', fontsize=10)
axs[2].grid(True, linestyle='-.', linewidth=0.8, alpha=0.5, axis='x')

plt.tight_layout()
plt.show()