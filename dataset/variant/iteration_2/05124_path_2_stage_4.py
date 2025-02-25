import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
index_A = np.array([1150, 1000, 1080, 1020, 1120, 1050, 1200, 1170, 1250, 1180, 1220, 1280])
index_B = np.array([1020, 980, 1040, 1100, 1010, 1070, 1180, 1230, 1130, 1150, 1200, 1270])
index_C = np.array([1100, 950, 1250, 1300, 1000, 1050, 1140, 1025, 1100, 1150, 1200, 1350])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, index_A, marker='D', linestyle='--', linewidth=2.5, color='#3375FF')
ax.plot(months, index_B, marker='*', linestyle=':', linewidth=2.5, color='#FF5733')
ax.plot(months, index_C, marker='x', linestyle='-.', linewidth=2.5, color='#33FFB5')

ax.grid(linestyle='-', alpha=0.4)
plt.tight_layout()
plt.show()