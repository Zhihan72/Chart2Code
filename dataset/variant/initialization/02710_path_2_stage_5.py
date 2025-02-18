import matplotlib.pyplot as plt

# Randomly altered names for regions
regions = ['Apples', 'Europe', 'Zebras', 'North Pole', 'Bananas & Grapes', 'Oceania', 
           'Marsupials', 'Middle Earth']
usage_percentages = [53, 15, 12, 10, 7, 3, 0.5, 9.5]

colors = ['#33FFF9', '#FF33A8', '#FF5733', '#3357FF', '#F9FF33', '#33FF57', '#FFD700', '#FF6347']
explode = (0, 0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(12, 8))
plt.pie(usage_percentages, startangle=140, colors=colors,
        explode=explode, autopct='%1.1f%%')

# Randomly altered chart title
plt.title('Funky Distribution\n of Weather Patterns (2025)', fontsize=14, fontweight='medium')
plt.axis('equal')
plt.show()