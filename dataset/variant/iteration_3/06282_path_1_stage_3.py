import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

smart_meters_traffic = [50, 55, 60, 65, 75, 85, 95, 105, 110, 120, 125, 130]
security_cameras_traffic = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
connected_vehicles_traffic = [150, 160, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230]
smart_home_traffic = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
wearable_devices_traffic = [30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]

fig, ax = plt.subplots(figsize=(14, 8))

traffic_data = np.vstack([
    smart_meters_traffic, 
    security_cameras_traffic, 
    connected_vehicles_traffic, 
    smart_home_traffic, 
    wearable_devices_traffic
])

ax.stackplot(months, traffic_data, colors=['#FFB6C1', '#90EE90', '#FFA07A', '#ADD8E6', '#FFFFE0'], alpha=0.8)

ax.set_xticks([])
ax.set_yticks([])

ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()