from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	ls = []
	for i in range(number):
		ls.append(random.randint(-1000,1000))
	return ls
	pass

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array

	array = gen_random_int(number, seed)
	pass

	# array = None
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ', '.join(array) + '.'
	pass

	# array_str = None

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def bubblesort(array):
	n = len(array)
	swapped = True
	while swapped:
		swapped = False
		new_n = 0
		for inner_index in range(1, n):
			if array[inner_index] < array[inner_index-1]:
				array[inner_index], array[inner_index-1] = array[inner_index-1], array[inner_index]
				swapped = True
				new_n = inner_index
		n = new_n
	return array


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
	array_str = array_str[:-1].split(", ")

	for i in range(len(array_str)):
		array_str[i] = int(array_str[i])
	
	# n = len(array_str)
	# swapped = True
	# while swapped:
	# 	swapped = False
	# 	new_n = 0
	# 	for inner_index in range(1, n):
	# 		if array_str[inner_index] < array_str[inner_index-1]:
	# 			array_str[inner_index], array_str[inner_index-1] = array_str[inner_index-1], array_str[inner_index]
	# 			swapped = True
	# 			new_n = inner_index
	# 	n = new_n

	array_str = bubblesort(array_str)

	for i in range(len(array_str)):
		array_str[i] = str(array_str[i])

	array_str = ", ".join(array_str) + "."
	
	pass

	#array_str = None
	
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

	value = value.rstrip()
	value = value.split(",")

	for i in range(len(value)):
		value[i] = int(value[i])

	value = bubblesort(value)

	pass

	for i in range(len(value)):
		value[i] = str(value[i])

	array_str = ",".join(value)

	# array_str = None

	document.getElementById("sorted").innerHTML = array_str


