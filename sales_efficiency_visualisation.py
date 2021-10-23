from mimesis import Datetime
from mimesis import Address
from mimesis import random
from random import Random
import matplotlib.pyplot as pyplot


send_date=Datetime('uk')
dest_path=Address('uk')
send_number=Random()
array_send_dates=[]
array_dest_paths=[]
array_send_numbers=[]

for _ in range(0,10):
    array_send_dates.append(send_date.datetime(2000,2003,None))

for _ in range(0,9):
    array_dest_paths.append(dest_path.city())
print (array_dest_paths)

for _ in range(0,100):
    array_send_numbers.append(send_number.randint(1000,197000))
print (array_send_numbers)


#pyplot.title("Linear plot of send dates to target paths",fontsize=17,fontweight="bold",color="black")
#pyplot.xlabel("Send date",fontsize=14,color="black")
#pyplot.ylabel("Destination path",fontsize=14,color="black")
#pyplot.plot(array_dest_paths,array_send_dates)
#pyplot.grid()
#pyplot.barh(array_send_dates,array_dest_paths)
fig,(ax1,ax2)=pyplot.subplots(1,2,sharex=True,sharey=True)

ax1.plot(array_send_dates,ar)

