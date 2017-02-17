# from timeit import default_timer as timer
# import matplotlib.pyplot as plt


# # dict_name = {'hello': 'goodbye', 'interested': 'bored'}
# # for k in dict_name.keys():
    # # print(str(k) + ': ' + str(dict_name[k]))
# # del(dict_name['hello'])
# # for k in dict_name.keys():
    # # print(str(k) + ': ' + str(dict_name[k]))

# # help('string'.find('dick'))

# # horsemen = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]] 
# # del(horsemen[1])
# # print(str(horsemen))

# import random 

# # high = 100
# # low = 10

# # for i in range(10): 

	# # x = random.random() * 100
	# # if x < 10: x += 10
	# # print(str(x))

# #writing a program to divide the range into buckets and count the number of values in each.

# start = timer()
# # ...


# def randomlist(n):
	# s = [0] * n
	# for i in range(n):
		# s[i] = random.random()
		# #print(str(s[i]))
	# return s
	
# # def countthis(thing_to_count):
	
	# # count_1_quarter = 0
	# # count_2_quarter = 0
	# # count_3_quarter = 0
	# # count_4_quarter = 0
	
	# # for each in thing_to_count:
		
		# # # print('each: ' + str(each))
		
		# # if 0 <= each < 0.25: count_1_quarter += 1
		# # if 0.25 <= each < 0.50: count_2_quarter += 1
		# # if 0.50 <= each < 0.75: count_3_quarter += 1
		# # if 0.75 <= each <= 1: count_4_quarter += 1
		
		# # # print('1: ' + str(count_1_quarter))
		# # # print('2: ' + str(count_2_quarter))
		# # # print('3: ' + str(count_3_quarter))
		# # # print('4: ' + str(count_4_quarter))
		
	# # return count_1_quarter, count_2_quarter, count_3_quarter, count_4_quarter
	
# # def countthisway(low, high, thing_to_count):
	
	# # count = 0 
	
	# # for each in thing_to_count:
		
		# # # print('each: ' + str(each))
		
		# # if low <= each < high: count += 1
		
	# # return count

# # random_list = randomlist(10000) # Does not store the value! It runs it an returns it each time the name is referenced. 
# # # print('random_list: ' + str(random_list))
	
# # bucket1 = countthisway(0, 0.25, random_list)
# # bucket2 = countthisway(0.25, 0.50, random_list)
# # bucket3 = countthisway(0.50, 0.75, random_list)
# # bucket4 = countthisway(0.75, 1.0, random_list)
	
# # print('1: ' + str(bucket1) + ' 2: ' + str(bucket2) + ' 3: ' + str(bucket3) + ' 4: ' + str(bucket4))

# # def inBucket(thing_to_count, numBuckets):

	# # interval = 1 / numBuckets
	# # bucket_list = []
	# # low = 0 
	# # high = 0
	
	# # for bucket in range(0, numBuckets):
		
		# # low += interval 
		# # if high == 0: low = 0
		# # high += interval
		# # count = 0
		
		# # for each in thing_to_count:
			
			# # #print('low: ' + str(low))
			# # #print('high: '+ str(high))
			# # if low <= each < high:
				
				# # count += 1
		
		# # bucket_list.append({'Bucket {}'.format(bucket): count})
	
	# # return bucket_list
	
# # def inBucket(thing_to_count, numBuckets):

	# # interval = 1 / numBuckets
	# # bucket_list = []
	# # low = 0 
	# # high = 0
	
	# # for bucket in range(0, numBuckets):
		
		# # low = bucket * interval 
		# # high = low + interval
		# # count = 0
		
		# # for each in thing_to_count:
			
			# # #print('low: ' + str(low))
			# # #print('high: '+ str(high))
			# # if low <= each < high:
				
				# # count += 1
		
		# # bucket_list.append({'Bucket {}'.format(bucket + 1): count})
	
	# # return bucket_list
	
# def histogram(numBuckets):

	# interval = 1 / numBuckets
	# bucket_list = []
	# low = 0 
	# high = 0
	
	# for bucket in range(0, numBuckets):
		
		# low = bucket * interval 
		# high = low + interval
		# count = 0
		
		# bucket_list.append(low)
		
	# bucket_list.append(high)
	
	# return bucket_list

# plt.hist(randomlist(10000), histogram(4), histtype='bar', rwidth=0.8)

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
	
# end = timer()
# print('Time! Is: ' + str(end - start))
#print('The buckets! ' + str(inBucket(randomlist(100), 20)))

# Coming back to this later.

# def fibonacci (n): 
  
  # if n == 0 or n == 1: 
    # return 1 
  # else:
    # return fibonacci(n-1) + fibonacci(n-2) 
    

# print(fibonacci(1))


# def fibonothing (n): 
  
  # return n
    

# print(fibonothing(20))


# def compare(x, y):
	# if x > y:
		# return 1
	# if x == y:
		# return 0
	# if x < y:
		# return -1
		
# These 2 compare() functions are equivalent!
		
# def compare(x, y):
	# if not x < y:
		# return 1
	# if not x != y:
		# return 0
	# if not x > y:
		# return -1
		
# print(compare(65, 65))


# def hypotenuse(leg1, leg2):
	
	# hypotenuse =  (leg1**2 + leg2**2)**(1/2) 
	# return hypotenuse

# print(hypotenuse(1000, -7))
# # I finished the code after 3 lines... 


# Stage = each time I* run it

# def hypotenuse(a, b):

	# c = math.sqrt.(a**2, b**2)
	# return c
	
# print(hypotenuse(3,4))

# 1. SyntaxError: invalid syntax. Let's try this again. (Though I did import math the first time.)

# import math

# def hypotenuse(a, b):

	# c = math.sqrt.(a**2, b**2)
	# return c
	
# print(hypotenuse(3,4))

# 2. SyntaxError: invalid syntax. Removing 'math'.

# import math

# def hypotenuse(a, b):

	# c = sqrt.(a**2, b**2)
	# return c
	
# print(hypotenuse(3,4))

# 3. SyntaxError: invalid syntax. Looking up how to call the math module. 

# from math import sqrt

# def hypotenuse(a, b):

	# c = sqrt.(a**2, b**2)
	# return c
	
# print(hypotenuse(3,4))

# 4. SyntaxError: invalid syntax. Trying the function style call Also using the plus operator instead of a comma. 

# from math import sqrt

# def hypotenuse(a, b):

	# c = sqrt((a**2 + b**2))
	# return c
	
# print(hypotenuse(3,4))	

# 5. Returns 5.0 :) Truncating the return

# from math import sqrt

# def hypotenuse(a, b):
 
	# return sqrt((a**2 + b**2))
	
# print(hypotenuse(3,4))	

# 6. Returns 5.0. Switching to a sqrt that doesn't use the math module

# def hypotenuse(a, b):
 
	# return (a**2 + b**2)**(1.0/2.0)
	
# print(hypotenuse(3,4))	

# 7. Code truncated pretty deeply. Switching 1.0/2.0 to 0.5 for even shorterness. 

# def hypotenuse(a, b):
 
	# return (a**2 + b**2)**(0.5)
	
# print(hypotenuse(3,4))	


# Auto-schedule my day

# 14 hours
# Relaxation distributed evenly between work sessions

# Go to bed 20 hours from now

# Time stamp for start | Work or relaxation session | Time stamp for endswith

# def autoschedule(workhours, worksessionlength, hours_available): #, start_hour):

	# number_of_work_or_relax_sessions = int(workhours / worksessionlength)
	# relaxsessionlength = (hours_available - workhours) / number_of_work_or_relax_sessions * 60
	
	# work = str(number_of_work_or_relax_sessions), 'work sessions of', str(worksessionlength) + ' hours long.'
	# relax = str(number_of_work_or_relax_sessions), 'relaxation sessions of', str(int(relaxsessionlength)), 'minutes long.'
	# return  work, relax
	
	# #for each in range(0, hours_available)
	

# for each in autoschedule(14, 2, 20):
	# print(each)
	
# 1. Works for overview. Working on a while loop to get the result. 

# import time

# def autoschedule(workhours, worksessionlength, hours_available): #, start_hour):

	# number_of_work_or_relax_sessions = int(workhours / worksessionlength)
	# relaxsessionlength = (hours_available - workhours) / number_of_work_or_relax_sessions * 60
	
	# #work = str(number_of_work_or_relax_sessions), 'work sessions of', str(worksessionlength) + ' hours long.'
	# #relax = str(number_of_work_or_relax_sessions), 'relaxation sessions of', str(int(relaxsessionlength)), 'minutes long.'
	# #return  work, relax
	
	# schedule = [('teststart', 'testthingtodo', 'testend')]
	
	# count = 0
	
	# while number_of_work_or_relax_sessions > count:
		
		# if count == 0: work_start = time.time()
		# thing_to_do = 'Work'
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		# work_end = time.time() + worksessionlength * 3600
		# print('work_end id: ' + str(id(work_end)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# relax_start = work_end
		# print('relax_start id: ' + str(id(relax_start)))
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end = work_end + relaxsessionlength * 60
		# print('relax_end id: ' + str(id(relax_end)))
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# work_start = relax_end
		# print('work_start id: ' + str(id(work_start)))
		
		# count += 1
	
	# return schedule
	# #for each in range(0, hours_available)
	

# for each in autoschedule(14, 2, 20):
	# print(each)
	
# 2. It's getting the schedule organized the way I* want it. It's getting the time into it, though incorrectly. Need to figure out: How to convert it into time stamps.

# import time
# from datetime import datetime

# def autoschedule(workhours, worksessionlength, hours_available): #, start_hour):

	# number_of_work_or_relax_sessions = int(workhours / worksessionlength)
	# relaxsessionlength = (hours_available - workhours) / number_of_work_or_relax_sessions * 60
	
	# schedule = [('teststart', 'testthingtodo', 'testend')]
	
	# count = 0
	
	# while number_of_work_or_relax_sessions > count:
		
		# if count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = time.time() + worksessionlength * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relaxsessionlength * 60
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# count += 1
	
	# return schedule
	# #for each in range(0, hours_available)
	

# for each in autoschedule(14, 2, 20):
	# print(each)

# 3. Got the time to convert to human readable numbers! Next: Make the while loop properly upgrade the time. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 60
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	

# for each in autoschedule(14, 2, 20):
	# print(each)
	
# 4. UnboundLocalError: local variable 'termination_count' referenced before assignment. Correct mis-spell of termination_count variable. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 60
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	

# for each in autoschedule(14, 2, 20):
	# print(each)

# 5. It works--except it doesn't properly add time after the work session. Correct that.

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	

# for each in autoschedule(14, 2, 20):
	# print(each)
	
# 6. It 100% works. Now improving it so it doesn't output something so tuply. Could probably put this into a text file, too. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# Where I learned to convert Unix time (epoch time) to datetime stamps: http://bit.ly/1i6GfgU	

# 7. 100% works. Less tuply. Now converting it to a CSV file, to upload to Google.

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# myfile = open('schedule.csv', 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(autoschedule(14, 2, 20))	

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 8. TypeError: 'str' does not support the buffer interface. Need to fix that.

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# myfile = open('schedule.csv', 'w')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(autoschedule(14, 2, 20))	

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	

# 9. It successfully writes it to the csv file. It turns out the 2nd parameter has a buffer function, that I'm unaware of. Next: Need to figure out how to create a new line after every tuple. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('ticker_data.csv', 'wb') as csvfile:
	# writer = csv.writer(csvfile)
	# for entry in autoschedule(14, 2, 20):
		# chunks = ''
		# for part in entry:
			# chunks = chunks + ',' + str(part)
		# writer.writerow(chunk)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	

# 10. NameError: name 'chunk' is not defined. Update chunk issues

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('ticker_data.csv', 'w') as csvfile:
	# writer = csv.writer(csvfile)
	# for entry in autoschedule(14, 2, 20):
		# print('entry: ' + str(entry))
		# chunk = ''
		# for part in entry:
			# print('chunk: ' + str(chunk))
			# chunk = chunk + ',' + str(part)
		# writer.writerow(chunk)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	

# 11. Delimiting each character in the string. Need to not do that. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('ticker_data.csv', 'w') as csvfile:
	# writer = csv.writer(csvfile)
	# for entry in autoschedule(14, 2, 20):
		# print('entry: ' + str(entry))
		# chunk = ''
		# for part in entry:
			# if chunk == '': chunk = str(part)
			# else: chunk = chunk + ',' + str(part)
			# print('chunk: ' + str(chunk))
		# writer.writerow(part)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 12. Delimiting each character in the text. And only giving me the first value in the tuple. Need to get the full string values, and give every value in the tuple, before line breaking.

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('schedule.csv', 'w') as fp:
    # a = csv.writer(fp, delimiter=',')
    # a.writerows(autoschedule(14, 2, 20))

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 13. It works! It submits the schedule to a CSV file, which can be uploaded to Google Sheets or Excel. Next, I need it to keep the past data, too. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# import pandas as pd

# # Read the CSV into a pandas data frame (df)
# #   With a df you can do many things
# #   most important: visualize data with Seaborn
# df = pd.read_csv('myfile.csv', sep=',')
# print(df)

# # Or export it in many ways, e.g. a list of tuples
# tuples = [tuple(x) for x in df.values] + autoschedule(14, 2, 20)

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('schedule.csv', 'w') as fp:
    # a = csv.writer(fp, delimiter=',')
    # a.writerows(tuples)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))		
	
# 14. FileNotFoundError: File b'myfile.csv' does not exist. Need to update the file. 
	
# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = time.time()
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# print('thing_to_do id: ' + str(id(thing_to_do)))
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		# print('work_end id: ' + str(id(work_end_time)))
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		# print('relax_start id: ' + str(id(relax_start_time)))
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		# print('thing_to_do_r id: ' + str(id(thing_to_do_r)))
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		# print('relax_end id: ' + str(id(relax_end_time)))
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		# print('work_start id: ' + str(id(work_start_time)))
		
		# termination_count += 1
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# import pandas as pd

# # Read the CSV into a pandas data frame (df)
# #   With a df you can do many things
# #   most important: visualize data with Seaborn
# df = pd.read_csv('schedule.csv', sep=',')
# print(df)

# # Or export it in many ways, e.g. a list of tuples
# tuples = [tuple(x) for x in df.values] + autoschedule(14, 2, 20)

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('schedule.csv', 'w') as fp:
    # a = csv.writer(fp, delimiter=',')
    # a.writerows(tuples)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 15. It works! Now remove the scaffolding. Have it print the start time and end time as a tuple at the beginning

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# absolute_start_time = time.time()
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = absolute_start_time
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		
		# termination_count += 1
	
	# absolute_start = datetime.fromtimestamp(int(absolute_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	# absolute_end = relax_end
	
	# schedule.insert(0, ('Schedule for: ', absolute_start, absolute_end))
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# import pandas as pd

# # Read the CSV into a pandas data frame (df)
# #   With a df you can do many things
# #   most important: visualize data with Seaborn
# df = pd.read_csv('schedule.csv', sep=',')

# # Or export it in many ways, e.g. a list of tuples
# tuples = [tuple(x) for x in df.values] + autoschedule(14, 2, 20)

# # myfile = open('schedule.csv', 'w')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(autoschedule(14, 2, 20))	

# with open('schedule.csv', 'w') as fp:
    # a = csv.writer(fp, delimiter=',')
    # a.writerows(tuples)

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 16. Got it to work! Except if the file doesn't exist, I* get a FileNotFoundError: File b'schedule.csv' does not exist. Try except the end. 

# import time
# from datetime import datetime

# def autoschedule(work_hours, work_session_length, hours_until_bed): #, start_hour):

	# relax_hours = hours_until_bed - work_hours

	# number_of_work_or_relax_sessions = int(work_hours / work_session_length) # The of sessions to work to meet my workhour quota. And because the number of relax sessions = the number of work sessions, I just make this object represent both of them. 
	
	# relax_session_length = relax_hours / number_of_work_or_relax_sessions # The amount of time to tack onto the end of each work session to account for relaxing. 
	
	# schedule = []
	
	# absolute_start_time = time.time()
	
	# termination_count = 0
	
	# while number_of_work_or_relax_sessions > termination_count:
		
		# if termination_count == 0: work_start_time = absolute_start_time
		# work_start = datetime.fromtimestamp(int(work_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	
		# thing_to_do = 'Work'
		
		# work_end_time = work_start_time + work_session_length * 3600
		
		# work_end = datetime.fromtimestamp(int(work_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((work_start, thing_to_do, work_end))
		
		# #########
		
		# relax_start_time = work_end_time
		
		# relax_start = datetime.fromtimestamp(int(relax_start_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# thing_to_do_r = 'Relax'
		
		# relax_end_time = work_end_time + relax_session_length * 3600
		
		# relax_end = datetime.fromtimestamp(int(relax_end_time)).strftime('%d-%m-%Y %H:%M:%S')
		
		# schedule.append((relax_start, thing_to_do_r, relax_end))
		
		# ##########
		
		# work_start_time = relax_end_time
		
		# termination_count += 1
	
	# absolute_start = datetime.fromtimestamp(int(absolute_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	# absolute_end = relax_end
	
	# schedule.insert(0, ('Schedule for: ', absolute_start, absolute_end))
	
	# return schedule
	# #for each in range(0, hours_until_bed)
	
# import csv

# import pandas as pd

# try:

	# # Read the CSV into a pandas data frame (df)
	# #   With a df you can do many things
	# #   most important: visualize data with Seaborn
	# df = pd.read_csv('schedule.csv', sep=',')

	# # Or export it in many ways, e.g. a list of tuples
	# tuples = [tuple(x) for x in df.values] + autoschedule(12, 2, 17.)

	# # myfile = open('schedule.csv', 'w')
	# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	# # wr.writerow(autoschedule(14, 2, 20))	

	# with open('schedule.csv', 'w') as fp:
		# a = csv.writer(fp, delimiter=',')
		# a.writerows(tuples)
		
# except FileNotFoundError: 

	# with open('schedule.csv', 'w') as fp:
		# a = csv.writer(fp, delimiter=',')
		# a.writerows(autoschedule(12, 2, 17))

# for each in autoschedule(14, 2, 20):
	# print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
# 17. Still works. Just need to have it work based on user input

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
		
		##########
		
		work_start_time = relax_end_time
		
		termination_count += 1
	
	absolute_start = datetime.fromtimestamp(int(absolute_start_time)).strftime('%d-%m-%Y %H:%M:%S')
	absolute_end = relax_end
	
	schedule.insert(0, ('Schedule for: ', absolute_start, absolute_end))
	
	return schedule
	#for each in range(0, hours_until_bed)

hours_to_bed = float(input('How many hours until bed: '))
work_session_length = float(input('How many hours do you want to work for each session: '))
hours_to_work = float(input('How many hours do you want to work today: '))
	
import csv
import pandas as pd

try:

	# Read the CSV into a pandas data frame (df)
	#   With a df you can do many things
	#   most important: visualize data with Seaborn
	df = pd.read_csv('schedule.csv', sep=',')

	# Or export it in many ways, e.g. a list of tuples
	tuples = [tuple(x) for x in df.values] + autoschedule(12, 2, 17.)

	# myfile = open('schedule.csv', 'w')
	# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	# wr.writerow(autoschedule(14, 2, 20))	

	with open('schedule.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(tuples)
		
except FileNotFoundError: 

	with open('schedule.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(autoschedule(hours_to_work, work_session_length, hours_to_bed))

for each in autoschedule(hours_to_work, work_session_length, hours_to_bed):
	print('{} | {} | {}'.format(each[0], each[1], each[2]))	
	
'''

How do I* know it broke?

It didn't keep changing its guess... it kept doing the same thing over and over again. 


'''