import matplotlib.pyplot as plt
import numpy as np

regions = ['NA', 'EU', 'Asia']
AI_rate = [45, 50, 60]
IoT_rate = [55, 65, 70]
BC_rate = [25, 35, 45]
QC_rate = [10, 20, 30]
VR_rate = [15, 25, 35]  # New technology data for VR

adoption_data = np.array([AI_rate, IoT_rate, BC_rate, QC_rate, VR_rate])
technologies = ['AI', 'IoT', 'BC', 'QC', 'VR']

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(15, 7))

x = np.arange(len(regions))
width = 0.15
single_color = '#2ca02c'  # Consistent color for all data groups

total_adoption = np.sum(adoption_data, axis=1)
ax2.pie(total_adoption, labels=technologies, colors=[single_color]*len(technologies), autopct='%1.1f%%', startangle=140)

for i in range(len(adoption_data)):
    ax1.bar(x + i * width, adoption_data[i], width, color=single_color)

ax1.set_xlabel('Reg', fontsize=12)
ax1.set_ylabel('Adopt Rate (%)', fontsize=12)
ax1.set_xticks(x + width * 2)
ax1.set_xticklabels(regions)

for i in range(len(adoption_data)):
    for j in range(len(regions)):
        ax1.annotate(f'{adoption_data[i, j]}%',
                     xy=(x[j] + i * width, adoption_data[i, j]),
                     xytext=(0, 3),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()