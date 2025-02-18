import matplotlib.pyplot as plt

# Data and labels
modes = ['Cars', 'EVs', 'Transit', 'Bikes', 'Walk', 'Other']
shares = [35, 15, 25, 10, 10, 5]
color = '#1E90FF'  # Consistent color for all data groups
explode = (0, 0.1, 0, 0, 0, 0)

# Create a donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(shares, labels=modes, colors=[color] * len(modes), explode=explode,
                                  autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))

# Customize autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

plt.show()