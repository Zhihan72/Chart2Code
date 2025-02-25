import matplotlib.pyplot as plt
import numpy as np

regions = ['N. America', 'Europe', 'Asia']
AI_adoption_rate = [45, 50, 60]
IoT_adoption_rate = [55, 65, 70]
Blockchain_adoption_rate = [25, 35, 45]

adoption_data = np.array([AI_adoption_rate, IoT_adoption_rate, Blockchain_adoption_rate])
technologies = ['AI', 'IoT', 'BC']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

sorted_indices = np.argsort(adoption_data, axis=1)
sorted_data = np.sort(adoption_data, axis=1)

sorted_regions = [[regions[i] for i in sorted_indices[j]] for j in range(len(sorted_indices))]

width = 0.2
colors = ['#ff7f0e', '#d62728', '#2ca02c']

for i in range(len(sorted_data)):
    indices = np.arange(len(sorted_regions[i])) + i * width
    ax1.bar(indices, sorted_data[i], width, label=technologies[i], color=colors[i])
    ax1.set_xticks(indices)
    ax1.set_xticklabels(sorted_regions[i])

ax1.set_title('Tech Rates by Region (2023)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Rate (%)', fontsize=12)
ax1.legend(title='Tech', fontsize=11, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for i in range(len(sorted_data)):
    for j in range(len(sorted_data[i])):
        ax1.annotate(f'{sorted_data[i, j]}%',
                     xy=(j + i * width, sorted_data[i, j]),
                     xytext=(0, 3),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10)

total_adoption = np.sum(adoption_data, axis=1)
ax2.pie(total_adoption, labels=technologies, colors=colors, autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})

ax2.set_title('Tech Breakdown (2023)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()