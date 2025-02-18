import matplotlib.pyplot as plt

regions_altered = ['Africa', 'Latin America & Caribbean', 'Oceania', 'Asia', 'Atlantis', 'Europe', 'Antarctica', 'North America']
usage_percentages_altered = [12, 7, 3, 53, 0.9, 15, 0.1, 10]
colors = ['#99FF99', '#FFD700', '#FFCC99', '#FF9999', '#8A2BE2', '#66B2FF', '#A9A9A9', '#FF6347']
explode = (0, 0.1, 0, 0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))  # Changed figure size to make it square
plt.pie(usage_percentages_altered, labels=regions_altered, autopct='%1.1f%%', startangle=45, colors=colors,
        explode=explode, shadow=False, wedgeprops={'edgecolor': 'black'})  # Slightly changed some properties

plt.title('2023 Global Net User Distribution by Region', fontsize=14, fontweight='normal')  # Changed title style
plt.grid(True, linestyle='--', linewidth=0.5)  # Added grid
plt.gca().set_prop_cycle(None)  # Removed color cycling to reset styles
plt.gca().spines['top'].set_linewidth(2)  # Adjusted border of the plot
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)

plt.tight_layout()
plt.show()