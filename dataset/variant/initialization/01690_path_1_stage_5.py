import matplotlib.pyplot as plt

shares = [30, 20, 15, 10, 10, 10, 5]
single_color = '#66b3ff'  
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    shares, 
    autopct='',  # Disable percentage text inside wedges
    startangle=140, 
    colors=[single_color] * len(shares),  
    explode=explode, 
    wedgeprops={'width': 0.3}
)

plt.show()