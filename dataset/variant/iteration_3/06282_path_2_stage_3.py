import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
smart_meters_traffic = [50, 55, 60, 65, 75, 85, 95, 105, 110, 120, 125, 130]
security_cameras_traffic = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
connected_vehicles_traffic = [150, 160, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230]
smart_home_traffic = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

fig, ax = plt.subplots(figsize=(14, 8))

traffic_data = np.vstack([smart_meters_traffic, security_cameras_traffic, connected_vehicles_traffic, smart_home_traffic])
ax.stackplot(months, traffic_data, colors=['#FFB6C1', '#90EE90', '#FFFFE0', '#ADD8E6'], alpha=0.8)

plt.xticks(rotation=45)

fig.patch.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()