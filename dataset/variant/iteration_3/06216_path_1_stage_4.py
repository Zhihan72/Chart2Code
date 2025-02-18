import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2030, 10)
pop_music = np.array([10, 20, 25, 30, 32, 35, 40])
rock_music = np.array([5, 15, 20, 25, 26, 27, 29])
hiphop_music = np.array([0, 0, 5, 10, 15, 20, 25])
jazz_music = np.array([20, 18, 15, 10, 7, 5, 3])

plt.figure(figsize=(14, 8))

plt.plot(decades, pop_music, marker='D', linestyle='--', color='orange', linewidth=3)
plt.plot(decades, rock_music, marker='v', linestyle='-.', color='purple', linewidth=2)
plt.plot(decades, hiphop_music, marker='x', linestyle='-', color='cyan', linewidth=2)
plt.plot(decades, jazz_music, marker='h', linestyle=':', color='pink', linewidth=2)

plt.grid(True, linestyle='-.', alpha=0.8)

plt.tight_layout()
plt.show()