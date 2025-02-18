import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(2100, 2210, 10)

robotics = [5, 12, 30, 60, 100, 150, 220, 300, 380, 480, 600]
space_travel = [60, 90, 120, 150, 160, 170, 180, 190, 195, 200, 210]
quantum_computing = [4, 10, 18, 30, 50, 80, 130, 190, 270, 350, 450]
cybernetics = [25, 40, 70, 90, 115, 130, 160, 210, 260, 320, 380]

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