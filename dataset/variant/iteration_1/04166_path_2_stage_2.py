import matplotlib.pyplot as plt

years = list(range(2000, 2021))
temp_atlantis = [15.3, 15.4, 15.8, 15.7, 16.0, 16.3, 16.4, 16.6, 16.7, 16.8, 17.0, 17.2, 17.3, 17.5, 17.6, 17.8, 18.0, 18.2, 18.3, 18.5, 18.7]
temp_el_dorado = [17.5, 17.6, 17.8, 17.8, 18.0, 18.1, 18.3, 18.5, 18.6, 18.8, 19.0, 19.1, 19.3, 19.4, 19.6, 19.7, 19.9, 20.0, 20.2, 20.4, 20.5]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, temp_atlantis, marker='o', linestyle='-', color='green', linewidth=2)
ax.plot(years, temp_el_dorado, marker='s', linestyle='--', color='orange', linewidth=2)

plt.title('Average Annual Temperature Changes in Atlantis and El Dorado (2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

plt.tight_layout()
plt.show()