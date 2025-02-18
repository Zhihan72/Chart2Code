import matplotlib.pyplot as plt
import numpy as np

years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature']
data = np.array([
    [15, 18, 22, 26],
    [20, 22, 24, 30],
    [30, 32, 34, 38],
    [25, 28, 30, 35],
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15
y = np.arange(len(years))
color = 'blue'

for i in range(len(categories)):
    ax.barh(y + i * bar_height, data[i], height=bar_height, color=color)

# Removed text annotations showing the data values
# Removed axis labels, title, and yticks labels

plt.tight_layout()
plt.show()