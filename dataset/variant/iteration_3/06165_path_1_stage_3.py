import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
months = range(1, 13)

temperature_data = np.array([
    [30.5, 32.1, 45.2, 55.3, 65.2, 75.1, 80.0, 78.9, 70.3, 59.2, 45.1, 35.4],
    [31.2, 33.0, 46.5, 56.0, 66.1, 76.0, 80.3, 79.5, 71.1, 60.0, 46.0, 36.0],
    [30.8, 32.5, 45.7, 55.8, 65.8, 75.7, 80.5, 79.0, 70.8, 59.8, 45.9, 35.8],
    [31.0, 33.2, 46.3, 56.3, 66.5, 76.5, 81.0, 79.7, 71.5, 60.5, 46.5, 36.3],
    [30.9, 32.8, 45.9, 55.6, 65.9, 75.6, 80.8, 78.8, 70.6, 59.5, 45.6, 35.7],
    [31.5, 33.5, 46.8, 56.8, 66.8, 76.8, 81.5, 80.0, 71.8, 60.8, 46.8, 36.8],
    [31.8, 33.9, 47.2, 57.2, 67.2, 77.2, 82.0, 80.5, 72.2, 61.2, 47.2, 37.2],
    [32.0, 34.0, 47.5, 57.5, 67.5, 77.5, 82.5, 81.0, 73.0, 62.0, 47.5, 37.5],
    [32.3, 34.3, 48.0, 58.0, 68.0, 78.0, 83.0, 81.5, 73.5, 62.5, 48.0, 38.0],
    [32.5, 34.5, 48.5, 58.5, 68.5, 78.5, 83.5, 82.0, 74.0, 63.0, 48.5, 38.5]
])

plt.figure(figsize=(14, 8))

# Manually adjusted line styles and markers
linestyles = ['--', '-.', '-', ':', '--', '-.', '-', ':', '--', '-.']
markers = ['s', 'd', 'v', '^', '<', '>', 'o', 'p', 'h', '*']

# Manually shuffled colors
colors = ['#e377c2', '#7f7f7f', '#1f77b4', '#ff7f0e', 
          '#17becf', '#9467bd', '#8c564b', '#2ca02c', 
          '#bcbd22', '#d62728']

for i, year in enumerate(years):
    plt.plot(months, temperature_data[i], marker=markers[i], linestyle=linestyles[i], color=colors[i], label=str(year))

plt.title("Exploring Springfield Temperatures: A Yearly Comparison Over 10 Years", fontsize=16, fontweight='bold')
plt.xlabel("Month Count", fontsize=12)
plt.ylabel("Temp Month Average (in Fahrenheit)", fontsize=12)
plt.xticks(months, ['January', 'Feb', 'March', 'Apr', 'May', 'June', 'July', 'August', 'Sept', 'October', 'Nov', 'December'], rotation=45)

# Adjusting grid style and borders
plt.grid(True, linestyle='-', alpha=0.8)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(title='Yearly Data', loc="upper right", fontsize='medium')
plt.tight_layout()
plt.show()