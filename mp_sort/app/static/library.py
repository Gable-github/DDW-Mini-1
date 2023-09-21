from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	array = []
	for _ in range(number):
		array.append(str(random.randint(-1000,1000)))
	return array

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = gen_random_int(number, seed)


	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	

	array_str = ', '.join(array) + '.'

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_str = document.getElementById("generate").innerHTML
	array_str = array_str[:-1]
	array_str = array_str.split(', ')
	for i in range(len(array_str)):
		array_str[i] = int(array_str[i])

	n = len(array_str)
	swapped = True
	last_index = n
	
	while swapped:
		tmp = 0
		swapped = False
		for i in range(1, last_index):
			# print(i)
			if array_str[i-1] > array_str[i]:
				array_str[i-1] , array_str[i] = array_str[i], array_str[i-1]
				swapped = True
				tmp = i
				# print(f"last, {last_index}")
				# print(array_str)
		last_index = tmp

	for i in range(len(array_str)):
		array_str[i] = str(array_str[i])

	array_str = ', '.join(array_str) + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	val_list = value.split(',')
	for i in range(len(val_list)):
		val_list[i] = int(val_list[i])

	n = len(val_list)
	
	for outer in range(1, n):
		index = outer
		tmp = val_list[outer]
		for inner in range(outer):
			print(val_list)
			if val_list[index-1] < val_list[index]:
				val_list[index] = val_list[index-1]
				index -= 1
			val_list[index] = tmp

	for i in range(len(val_list)):
		val_list[i] = str(val_list[i])

	array_str = ', '.join(val_list) + '.'

	document.getElementById("sorted").innerHTML = array_str


