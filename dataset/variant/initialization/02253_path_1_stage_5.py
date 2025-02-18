import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(2100, 2210, 10)

# Shuffle within each data group while preserving structure
robotics = [12, 30, 5, 100, 60, 220, 150, 380, 300, 600, 480]
space_travel = [150, 60, 200, 90, 120, 160, 210, 195, 190, 180, 170]
quantum_computing = [80, 130, 30, 4, 450, 50, 10, 190, 350, 270, 18]
cybernetics = [130, 210, 90, 260, 320, 25, 160, 40, 115, 70, 380]

data = np.array([robotics, space_travel, quantum_computing, cybernetics])

total_innovations = np.sum(data, axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(decades, data, labels=['Rob', 'Space', 'Quantum', 'Cyber'],
             colors=['#FF6347', '#4682B4', '#3CB371', '#DAA520'], alpha=0.7)
ax.plot(decades, total_innovations, label='Total Tech Advances',
        color='#8B0000', linestyle='-.', marker='^', linewidth=2.5)

ax.set_title('Tech Innovations Over Time', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade')
ax.set_ylabel('Innovation Units')
ax.legend(loc='upper right', title='Tech Areas', fontsize=9, title_fontsize=11)
ax.grid(True, linestyle=':', color='gray', alpha=0.7)

plt.tight_layout()
plt.show()