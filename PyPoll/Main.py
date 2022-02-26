# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 04:34:02 2022

@author: INTEL
"""

import os
import csv

#variables
candidates_list = []
total_votes = 0
vote_counts = []

from pathlib import Path
PyPoll = Path('C:/Users/INTEL/Desktop/Monash/MONU-VIRT-DATA-PT-01-2022-U-LOL/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')

with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    
 
    for row in csvreader:
        total_votes = total_votes + 1    
        candidate_name = row[2]
        if candidate_name in candidates_list:
            candidate_list_index = candidates_list.index(candidate_name)
            vote_counts[candidate_list_index] = vote_counts[candidate_list_index] + 1
        else:
            candidates_list.append(candidate_name)
            vote_counts.append(1)

percentages = []
win_counts = vote_counts[0]
winning_index = 0

for i in range(len(candidates_list)):
    vote_percentage = round(vote_counts[i]/total_votes*100,1)
    percentages.append(vote_percentage)

    if vote_counts[i] > win_counts:
        win_counts = vote_counts[i]
        winning_index = i
winner = candidates_list[winning_index]

print("Election Results")
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for i in range(len(candidates_list)):
    print(f'{candidates_list[i]}: {percentages[i]}% ({vote_counts[i]})' )

print('----------------------------')
print(f'Winner: {winner}')

from pathlib import Path
output_file = 'C:/Users/INTEL/Desktop/Monash/MONU-VIRT-DATA-PT-01-2022-U-LOL/02-Homework/03-Python/Instructions/PyPoll/Analysis/Summary.txt'

with open(output_file, 'w') as f:
   
    f.write('Election Results:\n')
    f.write('---------------------------- \n')
    f.write(f'Total Votes: {total_votes} \n')
    f.write('---------------------------- \n')
    for i in range(len(candidates_list)):
        f.write(f'{candidates_list[i]}: {percentages[i]}% ({vote_counts[i]}) \n')
        
    f.write('---------------------------- \n')
    f.write(f'Winner: {winner} \n')
    
