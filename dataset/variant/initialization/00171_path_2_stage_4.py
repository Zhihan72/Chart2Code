import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
ai_index = np.array([10, 15, 25, 35, 50, 70, 95, 125, 160, 200, 250])
blockchain_index = np.array([5, 10, 15, 25, 40, 60, 95, 130, 180, 245, 320])
iot_index = np.array([8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88])

# Additional made-up data
arvr_index = np.array([3, 9, 18, 30, 45, 65, 90, 120, 155, 195, 240])
quantum_index = np.array([1, 4, 10, 20, 35, 55, 80, 110, 145, 185, 230])

plt.figure(figsize=(14, 8))

# Apply changed colors
plt.plot(years, ai_index, marker='o', linestyle='-', linewidth=2.5, color='#E63946')
plt.plot(years, blockchain_index, marker='s', linestyle='--', linewidth=2.5, color='#F4A261')
plt.plot(years, iot_index, marker='^', linestyle='-.', linewidth=2.5, color='#2A9D8F')

plt.plot(years, arvr_index, marker='d', linestyle=':', linewidth=2.5, color='#264653')
plt.plot(years, quantum_index, marker='x', linestyle='-', linewidth=2.5, color='#1D3557')

plt.title('Tech Innovations (2013-2023)', fontsize=16, pad=20)
plt.xlabel('Yr', fontsize=12)
plt.ylabel('Index', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 351, 50))

plt.tight_layout()

plt.show()