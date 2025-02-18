import matplotlib.pyplot as plt

activities = ['Exercise', 'Family Time', 'Education', 'Entertainment', 'Rest', 'Community Service']
time_spent = [10, 15, 20, 25, 20, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
explode = (0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    time_spent, labels=activities, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, wedgeprops=dict(edgecolor='white'))

plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=12)

ax.set_title('Distribution of Time Spent on Weekend Activities\nin a Fictional Utopian Society in 2050', fontsize=16, weight='bold', pad=20)

ax.axis('equal')
plt.show()