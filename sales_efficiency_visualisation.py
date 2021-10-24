from mimesis import Datetime
from mimesis import Address
from mimesis import random
from random import Random
import matplotlib.pyplot as pyplot
import numpy as np
from numpy.lib import index_tricks
import pandas as pd
from openpyxl import Workbook
import csv

send_date=Datetime('uk')
dest_path=Address('uk')
send_number=Random()
array_send_dates=[]
array_dest_paths=[]
array_send_numbers=[]

for _ in range(0,3000):
    array_send_dates.append(send_date.datetime(2000,2003,None))

for _ in range(0,9):
    array_dest_paths.append(dest_path.city())
print (array_dest_paths)



for _ in range(0,3000):
    array_send_numbers.append(send_number.randint(1000,197000))
print (array_send_numbers)


#pyplot.title("Linear plot of send dates to target paths",fontsize=17,fontweight="bold",color="black")
#pyplot.xlabel("Send date",fontsize=14,color="black")
#pyplot.ylabel("Destination path",fontsize=14,color="black")
#pyplot.plot(array_dest_paths,array_send_dates)
#pyplot.grid()
#pyplot.barh(array_send_dates,array_dest_paths)
'''
array_records = [array_dest_paths]

df = pd.DataFrame(array_records)
df.to_excel(excel_writer = "C:/Users/Eugene/Desktop/Sales efficiency visualisation/records.xlsx")

pyplot.barh(array_send_dates,array_send_numbers)
pyplot.show()
'''
with open('C:/Users/Eugene/Desktop/Sales efficiency visualisation/records.csv', 'w',encoding='cp1251') as f:
    writer = csv.writer(f)
    
    for iter in range(3000):
        writer.writerow([array_send_dates[iter],array_send_numbers[iter]])
    for iter in range(0,9):    
        writer.writerow(array_dest_paths)
    