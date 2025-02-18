import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Randomly altered Innovation Index data while preserving the structure
ai_index = np.array([15, 10, 35, 25, 70, 50, 125, 95, 200, 160, 250])  # Switched some values around
blockchain_index = np.array([10, 5, 25, 15, 60, 40, 130, 95, 245, 180, 320])  # Switched some values around
iot_index = np.array([16, 8, 32, 24, 48, 40, 64, 56, 80, 72, 88])  # Switched some values around

plt.figure(figsize=(14, 8))

plt.plot(years, ai_index, marker='o', label='Artificial Intelligence', linestyle='-', linewidth=2.5, color='#FF5733')
plt.plot(years, blockchain_index, marker='s', label='Blockchain Technology', linestyle='--', linewidth=2.5, color='#33FF57')
plt.plot(years, iot_index, marker='^', label='Internet of Things', linestyle='-.', linewidth=2.5, color='#3357FF')

plt.title('Tech Innovations by ByteTech Inc. (2013-2023)\nInnovation Index Across Key Areas', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Innovation Index', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 351, 50))

plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title='Tech Area', title_fontsize='13')

plt.annotate('AI Breakthrough',
             xy=(2019, ai_index[6]), 
             xytext=(2015, ai_index[6] + 40),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05),
             fontsize=10, color='#FF5733')

plt.annotate('Blockchain Surge',
             xy=(2022, blockchain_index[9]), 
             xytext=(2017, blockchain_index[9] + 50),
             arrowprops=dict(facecolor='#33FF57', shrink=0.05),
             fontsize=10, color='#33FF57')

plt.tight_layout()

plt.show()