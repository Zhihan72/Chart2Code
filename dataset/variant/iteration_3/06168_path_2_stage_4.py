import matplotlib.pyplot as plt
import numpy as np

# Average growth percentages for different countries
average_growth = {
    'USA': np.mean([3.1, 2.8, 3.6, 4.0, 5.2, 3.8, 4.1, 4.7, 5.0, 4.5, 3.9, 4.3]),
    'China': np.mean([4.5, 4.2, 4.8, 5.0, 5.3, 4.9, 5.1, 5.4, 5.7, 5.8, 5.2, 5.0]),
    'India': np.mean([3.5, 3.6, 3.8, 4.1, 3.9, 4.0, 3.7, 4.2, 4.5, 4.3, 3.4, 3.9]),
    'Germany': np.mean([2.8, 2.9, 3.1, 3.3, 4.0, 3.5, 3.8, 3.6, 3.7, 3.9, 4.1, 3.8]),
    'Japan': np.mean([4.2, 4.1, 4.3, 4.6, 4.9, 4.8, 5.0, 4.5, 5.1, 4.8, 4.2, 4.7])
}

countries = list(average_growth.keys())
growth_values = list(average_growth.values())

fig, ax = plt.subplots(figsize=(10, 6))

# Manually shuffled colors for each country
colors = ['green', 'blue', 'orange', 'red', 'cyan']

# Creating a horizontal bar chart
ax.barh(countries, growth_values, color=colors, alpha=0.9)

ax.set_title('Average Solar Growth in 2045 by Country', fontsize=18, fontweight='regular')
ax.set_xlabel('Average Growth (%)', fontsize=12)
ax.set_ylabel('Countries', fontsize=12)

ax.grid(visible=True, linestyle='-.', linewidth=0.5, axis='x')

plt.tight_layout()
plt.show()