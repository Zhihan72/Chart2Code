import matplotlib.pyplot as plt

years = list(range(2010, 2021))
playstation_sales = [14.2, 13.3, 16.3, 14.9, 17.8, 18.5, 19.4, 20.0, 17.7, 14.4, 12.5]
xbox_sales = [10.3, 9.4, 11.6, 12.7, 13.8, 15.3, 14.7, 16.2, 15.4, 14.1, 13.5]
nintendo_sales = [8.8, 9.0, 10.7, 11.8, 12.3, 13.7, 16.3, 15.4, 14.2, 18.5, 20.1]

# Additional made-up data series
sega_sales = [5.1, 4.8, 5.7, 6.2, 6.9, 7.5, 8.0, 7.8, 7.1, 6.8, 7.0]
atari_sales = [3.5, 3.7, 3.9, 4.1, 4.0, 4.5, 4.9, 5.0, 4.8, 4.3, 4.2]

sales_data = [playstation_sales, xbox_sales, nintendo_sales, sega_sales, atari_sales]

fig, ax = plt.subplots(figsize=(12, 7))
ax.boxplot(sales_data, vert=False, patch_artist=True)

ax.set_xlabel('Sales (Millions)', fontsize=14)
ax.set_yticklabels(['PlayStation', 'Xbox', 'Nintendo', 'Sega', 'Atari'], fontsize=12)

plt.tight_layout()
plt.show()