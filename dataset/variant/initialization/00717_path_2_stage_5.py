import matplotlib.pyplot as plt

market_shares = [25, 20, 15, 10, 5, 10]
new_colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#FF9F40', '#C9CBCF']
explode = (0.1, 0, 0, 0, 0, 0)

plt.figure(figsize=(9, 6))
wedges, texts, autotexts = plt.pie(
    market_shares, 
    autopct='%1.2f%%', 
    startangle=100, 
    colors=new_colors, 
    explode=explode, 
    shadow=False
)

# Draw a circle at the center of pie to make it a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
plt.grid(True)
plt.show()