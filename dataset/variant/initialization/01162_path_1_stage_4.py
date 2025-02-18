import matplotlib.pyplot as plt

# Data for fuel consumption (liters per 100km) for different vehicle types from 2000 to 2020
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]
suvs = [12.0, 11.8, 11.5, 11.3, 11.0, 10.7, 10.5, 10.3, 10.0, 9.8, 9.5, 9.3, 9.0, 8.8, 8.5, 8.3, 8.0, 7.8, 7.5, 7.3, 7.0]
trucks = [14.0, 13.8, 13.6, 13.4, 13.2, 13.0, 12.8, 12.6, 12.4, 12.2, 12.0, 11.8, 11.6, 11.4, 11.2, 11.0, 10.8, 10.6, 10.4, 10.2, 10.0]

data = [sedans, suvs, trucks]

plt.figure(figsize=(8, 8))
plt.boxplot(data, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lavender', color='purple'),
            whiskerprops=dict(color='purple', linestyle='-'),
            capprops=dict(color='purple'),
            medianprops=dict(color='green', linestyle='-'),
            flierprops=dict(markerfacecolor='blue', marker='^', markersize=10, linestyle='none'))

plt.grid(axis='y', linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()