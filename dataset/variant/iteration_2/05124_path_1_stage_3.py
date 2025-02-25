import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jn', 'Fb', 'Mr', 'Ap', 'Mj', 'Jn', 'Jl', 'Ag', 'Sp', 'Oc', 'Nv', 'Dc'])
index_A = np.array([1000, 1050, 1020, 1080, 1120, 1150, 1170, 1200, 1180, 1220, 1250, 1280])
index_B = np.array([980, 1020, 1010, 1040, 1070, 1100, 1130, 1150, 1180, 1200, 1230, 1270])
index_C = np.array([950, 1000, 1050, 1025, 1100, 1140, 1100, 1150, 1200, 1250, 1300, 1350])

fig, ax = plt.subplots(figsize=(16, 9))

common_color = '#3498db'
ax.plot(months, index_A, marker='o', linestyle='-', linewidth=2, color=common_color)
ax.plot(months, index_B, marker='^', linestyle='-', linewidth=2, color=common_color)
ax.plot(months, index_C, marker='s', linestyle='-', linewidth=2, color=common_color)

# Altered title and axis labels
ax.set_title('Market Series Fluctuation', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Time Segments', fontsize=16)
ax.set_ylabel('Metrics', fontsize=16)

plt.tight_layout()
plt.show()