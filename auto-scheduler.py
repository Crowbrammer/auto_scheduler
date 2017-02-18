# from timeit import default_timer as timer
# import matplotlib.pyplot as plt

import time
from datetime import datetime

def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	relax_hours = hours_until_bed - work_hours

	number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	schedule = []
	
	absolute_start_time = time.time()
	
	termination_count = 0
	
	while number_of_work_or_relax_sessions > termination_count:
		
		if termination_count == 0: work_start_time = absolute_start_time
		work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		thing_to_do = 'Work'
		work_end_time = work_start_time + work_session_length * 3600
		work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		schedule.append((work_start, thing_to_do, work_end))
		
		#########
		
		relax_start_time = work_end_time
		relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		thing_to_do_r = 'Relax'
		relax_end_time = work_end_time + relax_session_length * 3600
		relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		schedule.append((relax_start, thing_to_do_r, relax_end))
		work_start_time = relax_end_time
		termination_count += 1
	
	absolute_start = datetime.fromtimestamp(int(absolute_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	absolute_end = relax_end
	
	schedule.insert(0, ('Schedule for: ', absolute_start, absolute_end))
	
	return schedule

hours_to_bed = float(input('How many hours until bed: '))
work_session_length = float(input('How many hours do you want to work for each session: '))
hours_to_work = float(input('How many hours do you want to work today: '))
	
import csv
import pandas as pd

try:

	df = pd.read_csv('schedule.csv', sep=',')

	tuples = [tuple(x) for x in df.values] + autoschedule(hours_to_work, work_session_length, hours_to_bed)

	with open('schedule.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(tuples)
		
except FileNotFoundError: 

	with open('schedule.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(autoschedule(hours_to_work, work_session_length, hours_to_bed))

for each in autoschedule(hours_to_work, work_session_length, hours_to_bed):
	print('{} | {} | {}'.format(each[0], each[1], each[2]))	