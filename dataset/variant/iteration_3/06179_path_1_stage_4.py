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

fig, ax = plt.subplots(figsize=(8, 7))

ax.boxplot(bmi_data, vert=True, labels=age_groups)

ax.set_xlabel("Age")
ax.set_ylabel("BMI")

plt.tight_layout()
plt.show()