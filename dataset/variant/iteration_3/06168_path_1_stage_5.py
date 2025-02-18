import matplotlib.pyplot as plt
import numpy as np

# Data: Total annual growth of solar production for countries
country_labels = ['USA', 'China', 'India', 'Japan']
total_growth = {
    'USA': sum([3.1, 2.8, 3.6, 4.0, 5.2, 3.8, 4.1, 4.7, 5.0, 4.5, 3.9, 4.3]),
    'China': sum([4.5, 4.2, 4.8, 5.0, 5.3, 4.9, 5.1, 5.4, 5.7, 5.8, 5.2, 5.0]),
    'India': sum([3.5, 3.6, 3.8, 4.1, 3.9, 4.0, 3.7, 4.2, 4.5, 4.3, 3.4, 3.9]),
    'Japan': sum([4.2, 4.1, 4.3, 4.6, 4.9, 4.8, 5.0, 4.5, 5.1, 4.8, 4.2, 4.7])
}

# Sort countries by total growth
sorted_growth = dict(sorted(total_growth.items(), key=lambda item: item[1], reverse=True))

fig, ax = plt.subplots(figsize=(10, 6))

# Create a sorted bar chart
ax.bar(sorted_growth.keys(), sorted_growth.values(), color='orange', edgecolor='navy', alpha=0.85)

# Titles and labels
ax.set_title('Total Annual Solar Growth 2045', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_xlabel('Countries', fontsize=14, color='darkred')
ax.set_ylabel('Total Growth %', fontsize=14, color='darkred')

plt.xticks(color='navy')
plt.tight_layout()
plt.show()