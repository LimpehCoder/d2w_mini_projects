from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
    result = []
    for i in range(number):
        result.append(i)
    random.Random(seed).shuffle(result)
    return result

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	pass

	array = None
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	array_str = None

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1(array):
    n = len(array)
    for out_index in range(1, n):
        inn_index = out_index
        while inn_index > 0 and array[inn_index] < array[inn_index - 1]:
            array[inn_index], array[inn_index - 1] = array[inn_index - 1], array[inn_index]
            inn_index -= 1
    return array

	array_str = None
	
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
	pass

	array_str = None

	document.getElementById("sorted").innerHTML = array_str


