import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('seaborn')




year,total,men,women = np.loadtxt('prisoner.csv',unpack=True,delimiter = ',')


plt.plot(year,total,color='green',marker='o')
plt.xticks([1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
plt.text(2006,200000 , '1998 prisoner/population rate 0.001022525\n2017 prisoner/population rate 0.029100701');
plt.xlabel("Year")
plt.ylabel("Prisoner Number")
plt.title("Turkey's Total Prisoners")
plt.show()


plt.plot(year,men,color='red',marker='o')
plt.xticks([1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
plt.xlabel("Year")
plt.ylabel("Prisoner Number")
plt.title("Turkey's Male Prisoners")
plt.show()




plt.plot(year,women,color='blue',marker='o')
plt.xticks([1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
plt.xlabel("Year")
plt.ylabel("Prisoner Number")
plt.title("Turkey's Female Prisoners")
plt.show()
