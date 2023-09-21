from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	array = []
	random.seed(seed)
	for i in range(number):
		array.append(random.randint(-1000, 1000))

	print(array)
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
	array_str = ""
	for num in array:
		array_str += f"{num}, "
	
	array_str = array_str[:-2] + "."
	#print(array_str)

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
	unsorted_array_str = document.getElementById("generate").innerHTML

	unsorted_array = unsorted_array_str.strip().split(",")

	unsorted_array = [int(num) for num in unsorted_array]

	#print(unsorted_array)

	#sort using bubble
	n = len(unsorted_array)
	for i in range(n-1):
		for j in range(n-1):
			if unsorted_array[j] > unsorted_array[j+1]:
				#swap
				unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]

	sorted_array = unsorted_array
	#print(sorted_array)

	#Convert to string again
	array_str = ""
	for num in sorted_array:
		array_str += f"{num}, "
	
	array_str = array_str[:-2] + "."
	#print(array_str)

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
	#sort using bubble
	unsorted_array_str = value
	
	unsorted_array = unsorted_array_str.strip().split(",")

	unsorted_array = [int(num) for num in unsorted_array]

	#print(unsorted_array)

	#bubble sort
	n = len(unsorted_array)
	for i in range(n-1):
		for j in range(n-1):
			if unsorted_array[j] > unsorted_array[j+1]:
				#swap
				unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]

	sorted_array = unsorted_array
	#print(sorted_array)

	#Convert to string again
	array_str = ""
	for num in sorted_array:
		array_str += f"{num}, "
	
	array_str = array_str[:-2] + "."
	#print(array_str)

	document.getElementById("sorted").innerHTML = array_str


