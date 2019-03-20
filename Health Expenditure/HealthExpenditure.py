"""
TurkStat, Health Expenditure Statistics	
Indicators on health expenditures, 1999-2017	

"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('seaborn')
year,money = np.loadtxt('HealthExpenditure.csv',unpack=True,delimiter = ',')


plt.bar(year, money, color='green')
plt.xlabel("Year")
plt.ylabel("Health Expenditure (Million Turkish Lira)")
plt.title("Health Expenditure 1999-2017")


plt.xticks(year)
plt.show()



