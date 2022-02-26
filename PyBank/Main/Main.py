# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 02:03:55 2022

@author: INTEL
"""
import os
import csv

from pathlib import Path
pybank = Path('C:/Users/INTEL/Desktop/Monash/MONU-VIRT-DATA-PT-01-2022-U-LOL/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')



with open(pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    

    pybank_header = next(csv_reader)
    
    
    totalmonths = len(list(csv_reader))

   
    csv_file.seek(0)
    pybank_header = next(csv_reader)

    profit = 0
    for row in csv_reader:
        profit += float(row[1])
    csv_file.seek(0)
  
       
    pybank_header = next(csv_reader) 
    change = 0
    prev_profit = 0
    avg_profit = 0
    change_list = []
    profit_diff = []
    for row in csv_reader:
        change = float(row[1]) - prev_profit
        change_list.append(change)
        prev_profit = float(row[1])
    change_list.remove(change_list[0])
    avg_profit = sum(change_list) / (len(change_list))

   
    csv_file.seek(0)
    pybank_header = next(csv_reader)
    month_list = []
    for row in csv_reader:
        month_list.append(row[0])
       
    maxincrease = max(change_list)
    maxdecrease = min(change_list)

    maxincrease_month = change_list.index(maxincrease) + 1
    maxdecrease_month = change_list.index(maxdecrease) + 1
    
   
    print(f"Financial Analysis")
    print(f"--------------")
    print(f"Total Months:", totalmonths)
    print(f"Total: {profit}")
    print(f"Average Change: {round(avg_profit,2)}")
    print(f"Greatest Increase in Profits: {month_list[maxincrease_month]} (${(str(maxincrease))})")
    print(f"Greatest Decrease in Profits: {month_list[maxdecrease_month]} (${(str(maxdecrease))})")

from pathlib import Path
output_file = '../Analysis/Summary.txt'

with open(output_file, 'w') as f:
    
    
    f.write(f'Financial Analysis\n')
    f.write(f'--------------\n')
    f.write(f'Total Months: {(totalmonths)}\n')
    f.write(f'Total: {profit}"\n')
    f.write(f'Average Change: {round(avg_profit,2)}\n')
    f.write(f'Greatest Increase in Profits: {month_list[maxincrease_month]} (${(str(maxincrease))})\n')
    f.write(f'Greatest Decrease in Profits: {month_list[maxdecrease_month]} (${(str(maxdecrease))})\n')