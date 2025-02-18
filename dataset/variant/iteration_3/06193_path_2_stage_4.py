import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_upload_speeds = [12, 18, 15, 25, 10, 20, 8]
avg_download_speeds = [55, 50, 60, 52, 48, 58, 53]

plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(days, avg_upload_speeds, marker='s', linestyle='--', color='orange', linewidth=3, markersize=10)

# Plot download speeds
plt.plot(days, avg_download_speeds, marker='^', linestyle='-.', color='purple', linewidth=3, markersize=10)

plt.grid(True, linestyle=':', alpha=0.5)
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.ylim(0, 70)

plt.tight_layout()
plt.show()