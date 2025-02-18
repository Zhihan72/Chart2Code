import matplotlib.pyplot as plt
import numpy as np

# Data Preparation with manually altered yields
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
tomatoes_yield = np.array([19, 15, 17, 22, 16, 18, 20, 14, 23, 21])  # shuffled
carrots_yield = np.array([16, 12, 19, 13, 14, 14, 15, 18, 17, 19])  # shuffled
broccoli_yield = np.array([13, 8, 15, 9, 10, 14, 10, 11, 12, 14])   # shuffled

# Create the figure and a single subplot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the vegetable yields with new colors
ax.plot(years, tomatoes_yield, marker='o', linestyle='-', color='purple', linewidth=2, label='Tomatoes Yield')
ax.plot(years, carrots_yield, marker='s', linestyle='-', color='blue', linewidth=2, label='Carrots Yield')
ax.plot(years, broccoli_yield, marker='^', linestyle='-', color='cyan', linewidth=2, label='Broccoli Yield')

# Annotate the highest yield points in the shuffled data
annotations = {
    'Tomatoes': (2021, 23),
    'Carrots': (2022, 19),
    'Broccoli': (2015, 15),
}
for veg, (year, value) in annotations.items():
    ax.annotate(
        f'Peak: {value} tons',
        xy=(year, value),
        xytext=(-30, 10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='black'),
        fontsize=10,
        color='black'
    )

# Customize the plot
ax.set_title('Vegetable Yield Trends in Martindale (2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Yield (tons)', fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 25)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()