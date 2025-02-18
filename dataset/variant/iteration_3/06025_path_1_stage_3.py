import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a_2016 = np.array([3.1, 4.0, 7.5, 12.3, 17.9, 22.2, 25.5, 24.9, 20.3, 14.2, 9.1, 4.1])
city_a_2017 = np.array([2.9, 3.8, 7.7, 11.8, 17.5, 21.8, 25.2, 24.8, 20.1, 14.0, 8.8, 3.9])
city_a_2018 = np.array([3.0, 4.2, 7.6, 12.2, 18.0, 22.1, 25.7, 25.0, 20.4, 14.5, 9.2, 4.3])
city_a_2019 = np.array([3.2, 4.1, 7.8, 12.4, 18.1, 22.3, 25.9, 25.3, 20.7, 14.8, 9.4, 4.4])
city_a_2020 = np.array([3.3, 4.3, 8.0, 12.5, 18.3, 22.5, 26.0, 25.4, 20.9, 15.0, 9.6, 4.5])

city_b_2016 = np.array([10.1, 12.0, 17.5, 22.3, 27.9, 32.2, 35.5, 34.9, 30.3, 24.2, 18.1, 12.1])
city_b_2017 = np.array([10.0, 11.9, 17.4, 22.1, 27.8, 32.3, 35.8, 35.0, 30.5, 24.0, 18.0, 11.8])
city_b_2018 = np.array([10.2, 12.1, 17.6, 22.4, 28.0, 32.5, 36.0, 35.2, 30.7, 24.3, 18.3, 12.2])
city_b_2019 = np.array([10.5, 12.3, 17.8, 22.6, 28.2, 32.7, 36.2, 35.4, 30.9, 24.5, 18.5, 12.3])
city_b_2020 = np.array([10.6, 12.4, 17.9, 22.8, 28.3, 32.9, 36.3, 35.5, 31.0, 24.7, 18.6, 12.4])

city_c_2016 = np.array([5.4, 6.1, 12.0, 17.1, 22.0, 26.1, 29.7, 29.2, 24.5, 18.9, 12.5, 6.8])
city_c_2017 = np.array([5.2, 5.9, 11.8, 16.8, 21.8, 25.9, 29.4, 29.0, 24.2, 18.6, 12.3, 6.6])
city_c_2018 = np.array([5.3, 6.3, 12.2, 17.3, 22.1, 26.2, 29.9, 29.5, 24.8, 19.2, 12.8, 7.0])
city_c_2019 = np.array([5.5, 6.5, 12.5, 17.6, 22.4, 26.5, 30.2, 29.8, 25.1, 19.5, 13.1, 7.3])
city_c_2020 = np.array([5.6, 6.6, 12.6, 17.8, 22.7, 26.7, 30.5, 30.0, 25.3, 19.8, 13.4, 7.5])

plt.figure(figsize=(14, 8))

# City A plots
plt.plot(months, city_a_2016, marker='v', color='#17becf', linestyle='--')
plt.plot(months, city_a_2017, marker='s', color='#9467bd', linestyle='-.')
plt.plot(months, city_a_2018, marker='+', color='#bcbd22', linestyle=':')
plt.plot(months, city_a_2019, marker='x', color='#8c564b', linestyle='-')
plt.plot(months, city_a_2020, marker='D', color='#2ca02c', linestyle='--')

# City B plots
plt.plot(months, city_b_2016, marker='o', linestyle='-', color='#e377c2')
plt.plot(months, city_b_2017, marker='<', linestyle='--', color='#ff7f0e')
plt.plot(months, city_b_2018, marker='>', linestyle=':', color='#1f77b4')
plt.plot(months, city_b_2019, marker='^', linestyle='-.', color='#d62728')
plt.plot(months, city_b_2020, marker='h', linestyle='-', color='#7f7f7f')

# City C plots
plt.plot(months, city_c_2016, marker='*', linestyle='-', color='#aec7e8')
plt.plot(months, city_c_2017, marker='p', linestyle='--', color='#98df8a')
plt.plot(months, city_c_2018, marker='d', linestyle=':', color='#ffbb78')
plt.plot(months, city_c_2019, marker='H', linestyle='-.', color='#f7b6d2')
plt.plot(months, city_c_2020, marker='8', linestyle='-', color='#c5b0d5')

plt.xticks(rotation=45)
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.legend(['2016_A', '2017_A', '2018_A', '2019_A', '2020_A', 
            '2016_B', '2017_B', '2018_B', '2019_B', '2020_B',
            '2016_C', '2017_C', '2018_C', '2019_C', '2020_C'], loc='upper left', ncol=3)

plt.show()