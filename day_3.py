#!/usr/usr/python3
""" This module contains solution to
day 3 task
"""



def register_check(dict_param: dict) -> str:
	""" function that receives a dictionary
	containing students as argument, and prints
	'yes' if the student is in school and 'no'
	if the student is not in school. The function 
	should return the number of students in school. 
	"""
	students_in_attendance = list()
	for student in dict_param:
		if dict_param[student] == 'yes':
			students_in_attendance.append(student)
	return len(students_in_attendance)

#testing the function to see if it gives desired results
register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))