"""
		
TurkStat, Juveniles Received Into Security Unit, 2017	
Number of juveniles received into security units because of offence  					

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('seaborn')
year,total,boy,girl = np.loadtxt('juveniles.csv',unpack=True,delimiter = ',')


indexX = np.arange(len(year)) 
width = 0.35       
plt.bar(indexX, boy, width, color='#1B66D5',label='Boys')
plt.bar(indexX + width, girl, width,color='#D51BBC',label='Girls')



indexY=np.arange(21)
plt.yticks(indexY*5000)
plt.xticks(indexX + width / 2, ('2013', '2014', '2015', '2016', '2017'))
plt.legend(loc='best')


plt.ylabel('Juvenile Number')
plt.xlabel('Year')
plt.title('Juveniles Received Into Security Unit')

plt.show()


