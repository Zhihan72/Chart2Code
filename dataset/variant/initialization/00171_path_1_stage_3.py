import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

ai_index = np.array([15, 10, 35, 25, 70, 50, 125, 95, 200, 160, 250])
blockchain_index = np.array([10, 5, 25, 15, 60, 40, 130, 95, 245, 180, 320])
iot_index = np.array([16, 8, 32, 24, 48, 40, 64, 56, 80, 72, 88])

plt.figure(figsize=(12, 7))

plt.plot(years, ai_index, marker='v', label='Artificial Intelligence', linestyle='-', linewidth=2, color='#FF3333')
plt.plot(years, blockchain_index, marker='x', label='Blockchain Technology', linestyle='-', linewidth=2, color='#33FF33')
plt.plot(years, iot_index, marker='d', label='Internet of Things', linestyle='-', linewidth=2, color='#3333FF')

plt.title('Technology Innovation Trends 2013-2023', fontsize=14, pad=15)
plt.xlabel('Years', fontsize=11)
plt.ylabel('Innovation Index', fontsize=11)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 351, 50))

plt.grid(True, which='major', linestyle='-.', linewidth=0.6, alpha=0.8)
plt.legend(loc='lower right', fontsize=9, title='Categories', title_fontsize='11')

plt.annotate('AI Milestone',
             xy=(2019, ai_index[6]), 
             xytext=(2016, ai_index[6] + 30),
             arrowprops=dict(facecolor='#FF3333', arrowstyle='->', linestyle='dotted'),
             fontsize=9, color='#FF3333')

plt.annotate('Blockchain Increase',
             xy=(2022, blockchain_index[9]), 
             xytext=(2018, blockchain_index[9] + 40),
             arrowprops=dict(facecolor='#33FF33', arrowstyle='->', linestyle='dashed'),
             fontsize=9, color='#33FF33')

plt.tight_layout()

plt.show()