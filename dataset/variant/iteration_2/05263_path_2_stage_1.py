import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
AI_adoption_rate = [45, 50, 60]
IoT_adoption_rate = [55, 65, 70]
Blockchain_adoption_rate = [25, 35, 45]
Quantum_adoption_rate = [10, 20, 30]

adoption_data = np.array([AI_adoption_rate, IoT_adoption_rate, Blockchain_adoption_rate, Quantum_adoption_rate])
technologies = ['AI', 'IoT', 'Blockchain', 'Quantum Computing']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

x = np.arange(len(regions))
width = 0.2
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']

for i in range(len(adoption_data)):
    ax1.bar(x + i * width, adoption_data[i], width, color=colors[i])

ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Adoption Rate (%)', fontsize=12)
ax1.set_xticks(x + width * 1.5)
ax1.set_xticklabels(regions)

for i in range(len(adoption_data)):
    for j in range(len(regions)):
        ax1.annotate(f'{adoption_data[i, j]}%',
                     xy=(x[j] + i * width, adoption_data[i, j]),
                     xytext=(0, 3),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10)

total_adoption = np.sum(adoption_data, axis=1)
ax2.pie(total_adoption, labels=technologies, colors=colors, autopct='%1.1f%%', startangle=140)

plt.tight_layout()
plt.show()