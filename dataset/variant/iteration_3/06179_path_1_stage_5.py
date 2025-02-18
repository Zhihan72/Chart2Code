import matplotlib.pyplot as plt

age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65', '66-75', '76-85']

bmi_data = [
    [15, 16, 17, 18, 19, 20, 21, 22],
    [18, 20, 21, 22, 23, 24, 25, 27, 28],
    [19, 20, 22, 23, 24, 25, 26, 27, 29, 30],
    [22, 24, 26, 27, 28, 30, 32, 33],
    [25, 27, 29, 30, 32, 34, 35],
    [27, 28, 30, 32, 33, 34, 36, 38, 40],
    [29, 31, 32, 33, 35, 36, 37, 39],
    [32, 33, 35, 36, 37, 38, 40, 42]
]

fig, axs = plt.subplots(4, 2, figsize=(12, 10))  # Changed to 4 rows and 2 columns

for i, ax in enumerate(axs.flatten()):  # Flatten the 2D subplots array
    ax.boxplot(bmi_data[i], vert=True, labels=[age_groups[i]])
    ax.set_xlabel("Age")
    ax.set_ylabel("BMI")

plt.tight_layout()
plt.show()