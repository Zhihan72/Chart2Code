import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
ai_index = np.array([10, 15, 25, 35, 50, 70, 95, 125, 160, 200, 250])
blockchain_index = np.array([5, 10, 15, 25, 40, 60, 95, 130, 180, 245, 320])
iot_index = np.array([8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88])

plt.figure(figsize=(14, 8))

plt.plot(years, ai_index, marker='o', label='AI', linestyle='-', linewidth=2.5, color='#FF5733')
plt.plot(years, blockchain_index, marker='s', label='Blockchain', linestyle='--', linewidth=2.5, color='#33FF57')
plt.plot(years, iot_index, marker='^', label='IoT', linestyle='-.', linewidth=2.5, color='#3357FF')

plt.title('Tech Innovations (2013-2023)', fontsize=16, pad=20)
plt.xlabel('Yr', fontsize=12)
plt.ylabel('Index', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 351, 50))

plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title=None)

plt.annotate('AI Peak',
             xy=(2019, ai_index[6]), 
             xytext=(2015, ai_index[6] + 40),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05),
             fontsize=10, color='#FF5733')

plt.annotate('BC Spike',
             xy=(2022, blockchain_index[9]), 
             xytext=(2017, blockchain_index[9] + 50),
             arrowprops=dict(facecolor='#33FF57', shrink=0.05),
             fontsize=10, color='#33FF57')

plt.tight_layout()

plt.show()