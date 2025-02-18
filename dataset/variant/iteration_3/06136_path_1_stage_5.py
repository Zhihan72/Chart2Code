import matplotlib.pyplot as plt

activities = ['Leisure', 'Community Bonding', 'Learning', 'Recreation', 'Rejuvenation', 'Volunteer Work', 'Fitness', 'Creative Arts']
time_spent = [10, 15, 20, 25, 20, 10, 18, 12]
colors = ['#ffa07a', '#7fffd4', '#ff6347', '#4682b4', '#daa520', '#32cd32', '#ff1493', '#1e90ff']
explode = (0, 0, 0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))

# Plotting the donut chart with the specified 'width' in wedgeprops
wedges, texts, autotexts = ax.pie(
    time_spent, labels=activities, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, wedgeprops=dict(edgecolor='white', width=0.3))

plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=12)

ax.set_title('Weekend Time Allocation in a Hypothetical Society of 2060 with Additional Activities',
             fontsize=16, weight='bold', pad=20)

ax.axis('equal')
plt.show()