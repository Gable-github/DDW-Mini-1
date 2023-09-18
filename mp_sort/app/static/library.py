from org.transcrypt.stubs.browser import *
import random

# Global variable to store the array of random numbers
array = []

def gen_random_int(number, seed):
    random.seed(seed)
    return [random.randint(0, 10) for _ in range(number)]

def generate():
    global array  # Declare array as global so that we can modify it
    number = 10
    seed = 200

    # Call gen_random_int() with the given number and seed
    # Store it to the variable array
    array = gen_random_int(number, seed)

    # Convert the items into one single string
    # The numbers should be separated by a comma
    # And a full stop should end the string.
    array_str = ', '.join(map(str, array)) + "."

    # This line is to place the string into the HTML
    # Under div section with the id called "generate"
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

	array_str = None
	
	array_str = document.getElementById("generate").innerHTML

	array_str = array_str.replace(',','').replace('.','')

	sortedarray = list(map(int,array_str.split()))
	n = len(sortedarray)
	for i in range(1,n):
		for j in range(1,n):
			if sortedarray[j-1] > sortedarray[j]:
				sortedarray[j-1] , sortedarray[j] = sortedarray[j] , sortedarray[j-1]

	sortedarray = ', '.join(map(str, sortedarray))
	document.getElementById("sorted").innerHTML = sortedarray
	

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
    # The following line gets the value of the text input called "numbers"
    value = document.getElementById("numbers").value  # Changed from getElementsByName to getElementById

    # Throw an alert and stop if nothing is in the text input
    if value == "":
        window.alert("Your textbox is empty")
        return

    # Split the string using a comma as the separator and convert them to a list of numbers
    # Remove trailing whitespaces and convert the strings to integers
    sorted_array = [int(num.strip()) for num in value.split(',')]

    # Sort the list of numbers using bubble sort
    n = len(sorted_array)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_array[j] > sorted_array[j+1]:
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]

    # Create a single string containing the sorted numbers
    array_str = ', '.join(map(str, sorted_array))

    # Store it in array_str and update the HTML
    document.getElementById("sorted").innerHTML = array_str
