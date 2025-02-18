import matplotlib.pyplot as plt

populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]
populations_sundarban = [23, 25, 26, 24, 22, 23, 27, 29, 28, 30]
populations_kanha = [51, 49, 52, 54, 53, 55, 57, 56, 59, 60]

parks = ['Yellowstone', 'Sundarban', 'Kanha']
populations_data = [populations_yellowstone, populations_sundarban, populations_kanha]

plt.figure(figsize=(10, 6))
plt.boxplot(populations_data, vert=True, patch_artist=False)

plt.xticks([1, 2, 3], parks, fontsize=12)
plt.ylabel('Wildlife Numbers', fontsize=14)
plt.title('Ten-Year Trends in National Parks: Tiger Conservation Efforts', fontsize=16, weight='bold', pad=20)

plt.tight_layout()
plt.show()