import matplotlib.pyplot as plt

# Data and labels with altered shares
modes = ['Cars', 'EVs', 'Transit', 'Bikes', 'Walk', 'Other']
shares = [10, 25, 35, 15, 5, 10]  # Randomly altered but maintaining total sum
color = '#1E90FF'
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