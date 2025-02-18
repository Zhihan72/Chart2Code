import matplotlib.pyplot as plt

# Data and labels
modes = ['Cars', 'EVs', 'Transit', 'Bikes', 'Walk', 'Other']
shares = [35, 15, 25, 10, 10, 5]
colors = ['#8B0000', '#228B22', '#1E90FF', '#FFD700', '#FF6347', '#808080']
explode = (0, 0.1, 0, 0, 0, 0)

# Create a donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(shares, labels=modes, colors=colors, explode=explode,
                                  autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))

# Customize autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

plt.show()