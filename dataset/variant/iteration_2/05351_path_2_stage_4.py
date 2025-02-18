import matplotlib.pyplot as plt

years = list(range(2010, 2021))
playstation_sales = [14.2, 13.3, 16.3, 14.9, 17.8, 18.5, 19.4, 20.0, 17.7, 14.4, 12.5]
xbox_sales = [10.3, 9.4, 11.6, 12.7, 13.8, 15.3, 14.7, 16.2, 15.4, 14.1, 13.5]
nintendo_sales = [8.8, 9.0, 10.7, 11.8, 12.3, 13.7, 16.3, 15.4, 14.2, 18.5, 20.1]

sales_data = [playstation_sales, xbox_sales, nintendo_sales]

fig, ax = plt.subplots(figsize=(12, 7))
ax.boxplot(sales_data, vert=False, patch_artist=True)

ax.set_xlabel('Sales (Millions)', fontsize=14)
ax.set_yticklabels(['PlayStation', 'Xbox', 'Nintendo'], fontsize=12)

plt.tight_layout()
plt.show()