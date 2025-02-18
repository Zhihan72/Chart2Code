import matplotlib.pyplot as plt

# Data groups
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]
evs = [18.0, 17.5, 17.0, 16.5, 16.0, 15.5, 15.0, 14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0, 8.5, 8.0]
hybrids = [6.0, 5.8, 5.6, 5.5, 5.3, 5.1, 5.0, 4.8, 4.7, 4.5, 4.3, 4.2, 4.0, 3.9, 3.8, 3.6, 3.5, 3.4, 3.2, 3.1, 3.0]

plt.figure(figsize=(8, 6))
plt.boxplot(sedans, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightcoral', color='navy'),
            whiskerprops=dict(color='navy'),
            capprops=dict(color='navy'),
            medianprops=dict(color='darkorange', linewidth=2),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

plt.ylabel("Consumption (Ltr/100km)", fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['Sedans', 'EVs', 'Hybrids'])

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.show()